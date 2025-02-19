# Dimensionamento-Solar-CRM
O projeto Sistema de Dimensionamento Solar e CRM tem como objetivo fornecer uma solução eficiente, integrada e acessível para o dimensionamento de sistemas fotovoltaicos e a gestão do relacionamento com clientes.



COMPILAR (DIRETORIO Dimensionamento-Solar-CRM)
javac -d admin/model/bin -cp admin/model/lib/gson-2.11.0.jar admin/model/src/*.java

RODAR (DIRETORIO Dimensionamento-Solar-CRM)
java -cp admin/model/bin:admin/model/lib/gson-2.11.0.jar Main

RODAR O PY VIEW
python -m user.view.View

RODAR STREAMLIT
python -m streamlit run user/templates/Main.py
