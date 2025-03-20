# **TRABALHO DE GRAFOS**
## **Balde de Tinta - BFS e Vizinhança 8-Conectada**

### **Equipe:**
- **Mateus Levi**
- **Victor Rios**
- **Gabriel de Paula**
- **Cainã Rios**

---

### **Descrição**
Este trabalho apresenta a implementação da ferramenta **Balde de Tinta** utilizando **Busca em Largura (BFS)** e conectividade **8-conectada** para preenchimento de regiões em imagens representadas por matrizes.

A solução transforma a imagem em um **grafo**, onde cada pixel é um **nó** e suas conexões são baseadas na vizinhança 8-conectada. O preenchimento ocorre de forma eficiente utilizando a estrutura de dados **fila** para garantir a expansão correta da área.

---

### **Metodologia**
📌 **Leitura da Imagem:** Conversão para escala de cinza.  
📌 **Modelagem do Grafo:** Representação da matriz como um grafo implícito.  
📌 **Execução do Flood Fill:** Propagação usando BFS e vizinhança 8-conectada.  
📌 **Geração da Imagem Final:** Armazenamento e exibição dos resultados.

---

### **Ilustração da Conectividade**
#### **Vizinhança 4-Conectada (Manhattan)**
