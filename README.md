CareGuide Coach
A Multi-Agent Healthcare Education Assistant built with Google ADK, A2A Protocol & Vertex AI

Overview:  CareGuide Coach is a non-diagnostic, safe, multilingual healthcare education system. The system is built using Google ADK, multi agent architecture, API, SESSON AND MEMORY. The obserability and deployment of system using Vertex AI is implemented for gereated scope of use of the system. The multi agent architecture consist of orchestrator, intake,retrival, education and safety agents. along with it the custom tools integrated for great purformance include Healtcare API in assistance with built-in tools namely Google search and code Execution. CareGuide Coach provides Observability using Cloud Logging, Monitoring, and Trace along with A2A protocol. This project helps users understand chronic health conditions like diabetes, hypertension, etc., in simple language — without diagnosis or medical advice.

Problem CareGuide Coach Solves

Patients often receive complex information about chronic conditions but:
i) Don’t understand it fully
ii) Forget lifestyle instructions
iii) Need repeated explanation
iv) Lack a simple guide in their preferred language
v) Doctors don’t have time to repeat educational content.

Solution: CareGuide Coach provides : Condition education (explain diabetes, BP, HbA1c, etc.), General lifestyle recommendations, Red-flag detection (“seek medical help” guidance),Multilingual explanations (e.g., English + Hindi/Marathi),Context tracking per user session and Memory of user preferences

Note: Not a replacement for a doctor.
      Strict non-diagnostic, safety-first design.

Description: I Multi-Agent Architecture
1. Orchestrator Agent (Root)
i) Routes each user query
ii) Decides intent (education, follow-up, lifestyle guidance)
iii) Calls sub-agents via A2A

2. Intake & Context Agent
i) Cleans user input
ii) Extracts condition/topic
iii) Updates session state + long-term memory

3. Retrieval Agent

i) Calls Healthcare API (custom tool)
ii) Optionally uses Google Search (built-in tool)
iii) Can call Code Execution tool for simple calculations (BMI, categories)

4. Education Agent

i) Converts retrieved info into simple explanations
ii) Bilingual support
iii) Adds friendly guidance

5. Safety Agent

i) Prevents medical claims
ii) Adds disclaimers
iii) Flags red-flag symptoms with appropriate advice

If healthcare API provides Swagger spec

Sessions & Memory: i) InMemorySessionService for state
ii) Memory Bank for persistent preferences
iii)Context compaction to keep prompts small

Observability by using your Google Cloud free trials:
Cloud Logging → logs for agent transitions
Cloud Monitoring → metrics such as latency, agent usage
Cloud Trace → full request spans

Evaluation scripts simulate: Multiple users,Complex multi-turn conversations, Red-flag safety testing, Tool-failure recovery and Stored in /evaluation.
