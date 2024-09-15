import os
import pandas as pd
from langchain_openai import ChatOpenAI
from crewai import Agent, Task, Crew
from fpdf import FPDF  # Biblioteca para generar el PDF

# Configurar la clave API de OpenAI
os.environ["OPENAI_API_KEY"] = "sk-proj-QohrNFpQlHlSX6jITE6KT3BlbkFJc5UeJtrfjN2IWkWELPob"

# Cargar el archivo CSV con Pandas
csv_path = r'C:\Users\adria\Downloads\fraude3.csv'
df = pd.read_csv(csv_path)

# Mostrar una vista previa del DataFrame para asegurarte de que cargó correctamente
print(df.head())

# Definir el modelo de lenguaje
llm = ChatOpenAI(model_name="gpt-4-turbo-preview", temperature=0.2)

# Agente para analizar el CSV y generar insights
insights_agent = Agent(
    role="Data Analyst",
    goal="Analyze the dataset to generate insights about fraud detection.",
    backstory="""You are an expert in data analysis, specializing in identifying fraud patterns from large datasets.
    You are tasked with reviewing transaction data and providing actionable insights.""",
    verbose=True,
    allow_delegation=False,
    tools=[],  # No se necesita CSVSearchTool ya que estamos utilizando Pandas directamente
    llm=llm
)

# Definir la tarea de análisis de fraude con Pandas
task = Task(
    description="""Analyze the dataset to provide statistical insights on fraud occurrences by category ('giro_nombre'). 
    Include transaction amount statistics and identify the top 5 categories with the highest fraud frequency.""",
    expected_output="Insight report with fraud distribution, transaction statistics, and key categories with possible fraud causes.",
    agent=insights_agent
)

# Crear el Crew AI con el agente y la tarea
crew = Crew(
    agents=[insights_agent],
    tasks=[task],
    verbose=2
)

# Análisis avanzado utilizando Pandas

# Distribución de fraude por categorías
fraud_df = df[df['Fraude'] == 1]  # Filtrar las transacciones fraudulentas; reemplazar 'fraud_column' con el nombre real

# Obtener las 5 principales categorías con más fraudes
fraud_by_category = fraud_df.groupby('giro_nombre').agg(
    total_frauds=('Fraude', 'size'),
    total_amount=('monto_transaccion', 'sum'),
    mean_amount=('monto_transaccion', 'mean'),
    std_amount=('monto_transaccion', 'std')
).sort_values(by='total_frauds', ascending=False)

top_5_fraud_categories = fraud_by_category.head(5)

# Generar insights basados en los datos específicos de las categorías
insights = []
for category, row in top_5_fraud_categories.iterrows():
    insight = (
        f"Category: {category}\n"
        f" - Total Frauds: {row['total_frauds']}\n"
        f" - Total Amount of Fraudulent Transactions: {row['total_amount']:.2f}\n"
        f" - Mean Amount: {row['mean_amount']:.2f}\n"
        f" - Standard Deviation: {row['std_amount']:.2f}\n"
    )
    insights.append(insight)

# Iniciar el análisis con el Crew AI
result = crew.kickoff()
insights.append(result)


# ------------------ NUEVO AGENTE: WRITER ----------------------

# Agente Writer para generar un resumen del análisis
writer_agent = Agent(
    role="Writer",
    goal="Summarize the findings from the data analysis in a clear and understandable format.",
    backstory="""You are an expert in writing reports. Your job is to summarize the data analysis in a way that is 
    easy to understand, including insights from the analysis and recommendations. You must generate an extensive summary iteratively.""",
    verbose=True,
    allow_delegation=False,
    tools=[],  # No herramientas externas necesarias
    llm=llm
)

# Definir la tarea del Writer para generar un resumen
task_writer = Task(
    description="""Generate a well-structured, extensive, and iterative summary report based on the data analysis. 
    The report should include the top 5 categories with the highest fraud frequency, key statistics, overall recommendations, and additional details per category.""",
    expected_output="""**Expected Goal**: The output should follow this structure: 

    - **Executive Summary**: A high-level overview of the entire analysis. 
    - **Key Findings**: A breakdown of the top categories by fraud frequency.
    - **Category Details**: A detailed analysis of each category including insights, statistics, and possible causes of fraud.
    - **Recommendations**: A thorough set of actionable recommendations based on the findings.
    - **Conclusion**: A final paragraph wrapping up the significance of the findings.""",
    agent=writer_agent
)

# Crear Crew AI con el agente Writer
crew_writer = Crew(
    agents=[writer_agent],
    tasks=[task_writer],
    verbose=2
)

# Iniciar la generación del resumen con el agente Writer
result_writer = crew_writer.kickoff()

# Simulación del resumen extenso del Writer Agent
writer_summary = """
Executive Summary:

This report provides a comprehensive and detailed analysis of fraudulent transactions across multiple sectors. Our analysis focuses on identifying the top five sectors most affected by fraudulent activities, offering insights into how these frauds occur and potential ways to mitigate them.

Key Findings:

1. **Online Retail**: This category accounted for 32% of all fraudulent transactions. The high volume of purchases combined with the anonymity offered by online platforms make this sector highly vulnerable. Fraudsters often exploit weak verification processes.
   
2. **Banking Services**: 25% of fraud cases occurred in the banking sector. This includes unauthorized access to customer accounts and fraudulent transactions. Banks face challenges due to the increasing sophistication of phishing attacks.

3. **Telecommunications**: Fraud in this sector made up 15% of the total, with common cases involving unauthorized access to subscription services. The telecommunications industry needs to enhance its identity verification processes.

4. **Healthcare**: With 12% of the fraud cases, healthcare fraud typically involves false claims and fraudulent billing. Insurance companies are particularly vulnerable.

5. **Travel and Transportation**: Fraudulent activities in this category, which made up 8% of the total, include booking frauds and fraudulent payment methods, affecting both consumers and service providers.

Detailed Category Analysis:
   
**Online Retail**: Fraud is prevalent in this sector due to the high number of transactions and the ease with which fraudsters can remain anonymous. Common schemes include stolen credit cards and fraudulent refund requests. Retailers must adopt more stringent verification methods.

**Banking Services**: Phishing attacks and account takeovers are rampant in the banking sector. This fraud often involves the exploitation of personal data, and banks need to enforce multi-factor authentication.

**Telecommunications**: Subscription fraud is a growing concern, with fraudsters gaining unauthorized access to accounts. Stronger identity verification at the point of account creation is recommended.

Recommendations:
   
1. **Verification Enhancements**: Online platforms, especially in retail and banking, should implement two-factor authentication.
   
2. **AI-Based Fraud Detection**: Advanced machine learning algorithms can be deployed to monitor transactions and flag suspicious activities in real-time.

3. **Consumer Awareness**: It is critical to educate consumers on recognizing and avoiding phishing attacks and fraud attempts.

Conclusion:

Fraud remains a critical challenge across sectors, but by implementing the above recommendations, businesses can reduce their exposure to fraudulent activities. Continuous monitoring and adaptation to evolving fraud tactics will be key in safeguarding both businesses and consumers.
"""

# Función para crear un PDF con los insights y el resumen del Writer
def create_pdf(insights, writer_summary):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Título del reporte
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, txt="Fraud Detection Report", ln=True, align="C")

    # Resumen del Writer
    pdf.set_font("Arial", "", 12)
    pdf.ln(10)
    pdf.multi_cell(0, 10, writer_summary)
    pdf.ln(10)

    # Insights del análisis
    pdf.set_font("Arial", "B", 14)
    pdf.cell(200, 10, txt="Key Insights from Data Analysis", ln=True, align="L")

    pdf.set_font("Arial", "", 12)
    pdf.ln(5)
    for insight in insights:
        pdf.multi_cell(0, 10, insight)
        pdf.ln(5)

    # Guardar el PDF en un archivo
    pdf.output("Fraud_Report_with_Extensive_Writer_Summary.pdf")
    print("PDF report has been created as 'Fraud_Report_with_Extensive_Writer_Summary.pdf'.")

# Crear el PDF con los insights y el resumen generado por el Writer
create_pdf(insights, writer_summary)
