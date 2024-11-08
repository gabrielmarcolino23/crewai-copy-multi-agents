import os
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import DOCXSearchTool

from dotenv import load_dotenv
load_dotenv()

import agentops
agentops.init()


model = os.getenv("OPENAI_MODEL_NAME")
temperature = os.getenv("OPENAI_MODEL_TEMPERATURE")
llm = LLM(model=model, temperature=temperature)

@CrewBase
class CopywhatsappCrew():
	"""Copywhatsapp crew"""
	
	@agent
	def promptBuilder(self) -> Agent:
		return Agent(
			config=self.agents_config['promptBuilder'],
			verbose=True
		)
	
	@agent
	def variableSuggester(self) -> Agent:
		return Agent(
			config=self.agents_config['variableSuggester'],
			verbose=True
		)

	@agent
	def copywriter(self) -> Agent:
		return Agent(
			config=self.agents_config['copywriter'],
			# tools=[DOCXSearchTool(docx='docs/exemplos.docx')],
			verbose=True
		)

	@task
	def promptBuilder_task(self) -> Task:
		return Task(
			config=self.tasks_config['promptBuilder_task'],
		)
	
	@task
	def variableSuggester_task(self) -> Task:
		return Task(
			config=self.tasks_config['variableSuggester_task'],
		)
	
	@task
	def copywriter_task(self) -> Task:
		return Task(
			config=self.tasks_config['copywriter_task'],
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Copywhatsapp crew"""
		return Crew(
			agents=self.agents, 
			tasks=self.tasks, 
			process=Process.sequential,
			verbose=True,
			
		)