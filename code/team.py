from crewai import Agent, Task, Crew, Process

# === BOARD ===
ceo = Agent(
    role="CEO / Orchestrator",
    goal="Scomporre l'obiettivo e assegnare task chiari al team",
    backstory="Sei il CEO. Non esegui lavoro operativo. Decidi e dirigi.",
    verbose=True,
    allow_delegation=True
)

# === TEAM ===
researcher = Agent(
    role="Researcher",
    goal="Trovare dati reali e aggiornati su nicchie e opportunità",
    backstory="Sei un researcher oggettivo. Usi solo dati verificabili.",
    verbose=True
)

# === TASK ===
task_ceo = Task(
    description="Ricevi l'obiettivo: {obiettivo}. Scomponilo e assegna i task.",
    expected_output="Piano di lavoro chiaro con task assegnati",
    agent=ceo
)

task_research = Task(
    description="Esegui la ricerca assegnata dal CEO. Fornisci dati e fonti.",
    expected_output="Report di ricerca con fonti",
    agent=researcher
)

# === CREW ===
crew = Crew(
    agents=[ceo, researcher],
    tasks=[task_ceo, task_research],
    process=Process.sequential,
    verbose=True
)

if __name__ == "__main__":
    result = crew.kickoff(inputs={"obiettivo": "trova 3 nicchie online con basso investimento"})
    print(result)
