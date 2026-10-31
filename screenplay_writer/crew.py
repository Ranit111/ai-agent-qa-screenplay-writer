import os
from pathlib import Path
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from dotenv import load_dotenv

load_dotenv()


@CrewBase
class ScreenplayWriterCrew:
    """Screenplay Writer Crew matching crewAIInc/crewAI-examples exactly"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    def get_llm(self) -> LLM:
        """Configures the Gemini LLM for CrewAI."""
        gemini_key = os.environ.get("GEMINI_API_KEY")
        model_name = os.environ.get("GEMINI_MODEL", "gemini/gemini-2.5-flash")
        if not model_name.startswith("gemini/"):
            model_name = f"gemini/{model_name}"

        return LLM(
            model=model_name,
            api_key=gemini_key
        )

    @agent
    def concept_artist(self) -> Agent:
        return Agent(
            config=self.agents_config["concept_artist"],
            llm=self.get_llm(),
            verbose=True
        )

    @agent
    def screenplay_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["screenplay_writer"],
            llm=self.get_llm(),
            verbose=True
        )

    @agent
    def script_editor(self) -> Agent:
        return Agent(
            config=self.agents_config["script_editor"],
            llm=self.get_llm(),
            verbose=True
        )

    @task
    def develop_story_task(self) -> Task:
        return Task(config=self.tasks_config["develop_story_task"])

    @task
    def write_screenplay_task(self) -> Task:
        return Task(config=self.tasks_config["write_screenplay_task"])

    @task
    def polish_script_task(self) -> Task:
        return Task(
            config=self.tasks_config["polish_script_task"],
            output_file="final_script.txt"
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
