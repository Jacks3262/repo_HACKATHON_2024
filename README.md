# repo_HACKATHON_2024
Repositorio oficial del equipo Datacoders, donde se realizaron análisis para la organización de Capital One en el HACKATHON 2024.

## Integrantes del Equipo DataCoders
* Luis Maximiliano López Ramírez - A00833321
* Dilan González Castañeda - A00831905
* Rogelio Lizárraga Escobar - A01742161
* Adrian Pineda Sánxhez - A00834710

# Proyecto con Capital One

La problemática de fraudes en transacciones es un desafío creciente para empresas y consumidores a nivel global. A medida que las transacciones digitales se expanden y se diversifican, surgen nuevas oportunidades para los estafadores que buscan vulnerar los sistemas de pago. Los fraudes pueden manifestarse de diversas formas, desde el uso indebido de tarjetas de crédito hasta la suplantación de identidad y la manipulación de transacciones en plataformas en línea. Estos incidentes no solo generan pérdidas económicas significativas, sino que también erosionan la confianza de los clientes y dañan la reputación de las empresas afectadas.

# Solución

Para abordar la creciente problemática de fraudes en transacciones, una solución efectiva ha sido la implementación de herramientas de machine learning y el uso de TensorFlow para redes neuronales, las cuales permiten clasificar de manera eficiente las transacciones fraudulentas. Estas tecnologías analizan grandes volúmenes de datos en tiempo real, identificando patrones sospechosos y anomalías que podrían indicar un fraude. A través del aprendizaje supervisado y no supervisado, los modelos de machine learning se entrenan con datos históricos de transacciones, lo que les permite detectar comportamientos atípicos con alta precisión. TensorFlow, con su capacidad para desarrollar redes neuronales complejas, potencia la detección automatizada de fraudes mediante modelos de clasificación que aprenden continuamente y se adaptan a nuevas tácticas fraudulentas.

# Distribución de archivos

## Datasets

Aquí se encuentran los datasets generados a partir de los scripts.
* **fraud.csv**

## Scripts

Contiene los códigos en .py y .ipynb para solución de la problemática planteada.
* **Fraude.py:** Realiza la transformación del dataset original para la creación de columnas de interés generando **fraud.csv**
* **Modelos_Convencionales.ipynb:** A partir de **fraud.csv** se generan modelos convencionales de Machine Learning para la detección de transacciones fraudolentas.
* **Modelos_Hackathon.ipynb:** A partir de **fraud.csv** se generan varias redes neuronales con TensorFlow para la detección de transacciones fraudolentas obteniendo aquí el mejor modelo de predicción.
* **crew_ai_csv_decode.py:** Código de Python que utiliza LLM para generar reportes e insights de interés a partir de **fraud.csv**

## Demonstrations

Contiene el video demo de algunas pruebas del modelo de predicción de transacciones fruadolentas además de contener la presentación usada para exponer ante Capital One.
* **Final presentation.pdf**
* **Video_Hackathon_2.mp4**

## flask-react
