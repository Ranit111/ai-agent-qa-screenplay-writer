#!/usr/bin/env python
import sys
import os
from dotenv import load_dotenv

# Add parent directory to path so imports work cleanly
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from crew import ScreenplayWriterCrew

load_dotenv()


def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'A cyber-detective investigates stolen digital memories in neo-Tokyo.'
    }
    if len(sys.argv) > 1:
        inputs['topic'] = sys.argv[1]

    print(f"\n🎬 Starting ScreenplayWriterCrew for topic: {inputs['topic']}")
    crew_instance = ScreenplayWriterCrew().crew()
    result = crew_instance.kickoff(inputs=inputs)
    print("\n✨ Crew Execution Completed!")
    print(result)
    return result


if __name__ == "__main__":
    run()
