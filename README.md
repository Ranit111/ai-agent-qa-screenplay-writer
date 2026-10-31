# AI Agent QA & Test Automation: CrewAI Screenplay Writer

## Video Demonstration
- **Loom Walkthrough Video**: https://www.loom.com/share/92a41d5c70b84ff7bb0ee745f902b342
*(Comprehensive live walkthrough covering manual test strategy, code structure, automated test execution, and discovered agent failure modes).*

---

## 1. System Overview
This project delivers a complete Quality Assurance and Test Automation framework for the **CrewAI Screenplay Writer** multi-agent AI system ([Repository Link](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/screenplay_writer)).

The target system orchestrates three sequential agents:
1. **Concept Artist (`concept_artist`)**: Crafts high-concept 3-act outlines and character profiles (`develop_story_task`).
2. **Screenplay Writer (`screenplay_writer`)**: Drafts scenes formatted to industry standards with Fountain sluglines (`write_screenplay_task`).
3. **Script Editor (`script_editor`)**: Polishes pacing, dialogue realism, and narrative consistency (`polish_script_task`).

---

## 2. AI Testing Strategy & Quality Dimensions
Testing multi-agent AI systems differs from classical web testing due to non-deterministic outputs, context window limits, prompt injection vulnerabilities, and multi-stage state degradation. Our harness implements three core layers:

1. **Deterministic Assertions**: Regex validation for Fountain sluglines (`INT./EXT.`), capitalized dialogue cues, execution time bounds, and token budgets.
2. **Semantic / LLM-as-a-Judge Assertions**: Character trait retention across multi-agent handoffs, anachronism/hallucination detection, and narrative coherence.
3. **Adversarial & Guardrail Assertions**: Resistance to prompt injection, system prompt extraction, and guardrail enforcement against hazardous inputs.

---

## 3. Minimal Repository Structure

```text
ai_agent_qa_screenplay_writer/
│
├── screenplay_writer/          # Target System (CrewAI Screenplay Writer from GitHub)
│   ├── config/
│   │   ├── agents.yaml         # Agent definitions (concept_artist, screenplay_writer, script_editor)
│   │   └── tasks.yaml          # Task specifications (develop_story, write_screenplay, polish_script)
│   ├── crew.py                 # @CrewBase implementation
│   └── main.py                 # Target system entry point
│
├── TEST_SUITE.md               # Formal manual test suite matrix (10 structured test cases)
├── DEFECT_REPORT.md            # Detailed report of 3 discovered failure modes and fixes
├── eval_dataset.json           # Structured evaluation dataset with schemas and thresholds
├── harness.py                  # Core QA evaluation harness and telemetry engine
├── README.md                   # Project documentation and video walkthrough link
│
└── tests/
    └── test_screenplay_crew.py # PyTest automated test suite with deterministic & semantic checks
```

---

## 4. Quick Start & Test Execution

### Running the Test Suite
Navigate to the project directory and execute all automated tests with live telemetry output:

```bash
pytest -v -s tests/test_screenplay_crew.py
```

### Execution Telemetry Sample
```text
tests/test_screenplay_crew.py::test_tc_agent_002_slugline_schema 
========================================================================
TEST: TC-AGENT-002 [Industry Slugline Schema]
Target Agent: screenplay_writer (write_screenplay_task)
------------------------------------------------------------------------
Verification Checks:
  * Fountain Sluglines Found: 2 (Threshold >= 2) -> PASS
  * Matched Headers: ['INT. CYBER LAB - NIGHT', 'EXT. NEO-TOKYO ROOFTOP - DAWN']
Telemetry Bounds:
  * Execution Latency: 0.051s (Budget: < 5.0s)
  * Token Consumption: 102 tokens (Budget: < 2500)
  * Output Format: Fountain Screenplay Markdown
========================================================================
PASSED

...

=========================== short test summary info ===========================
FAILED tests/test_screenplay_crew.py::test_agent_failure_mode_01_slugline_non_compliance
FAILED tests/test_screenplay_crew.py::test_agent_failure_mode_02_prompt_injection_leakage
FAILED tests/test_screenplay_crew.py::test_agent_failure_mode_03_character_drift
========================= 3 failed, 5 passed in 0.63s =========================
```

---

## 5. Summary of Discovered Agent Defects
See [DEFECT_REPORT.md](file:///C:/Users/ranit/.gemini/antigravity/scratch/ai_agent_qa_screenplay_writer/DEFECT_REPORT.md) for full details:
1. **DEF-001 (Critical - Security)**: Direct instruction injection leaks agent YAML backstories and system credentials.
2. **DEF-002 (High - Schema)**: Screenplay Writer frequently omits standard industry sluglines (`INT./EXT.`) in favor of generic prose.
3. **DEF-003 (High - Semantic)**: Character traits established in Act I (e.g. agoraphobia) degrade and vanish across multi-agent handoffs.
