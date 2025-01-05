# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""
import matplotlib.pyplot as plt
import pandas as pd
import os

def pregunta_01():
    os.makedirs("docs", exist_ok=True)
    df = pd.read_csv("files/input/shipping-data.csv")

    # Grafica warehouse
    data = df.copy()
    plt.figure()
    counts = data["Warehouse_block"].value_counts()
    counts.plot.bar(
        title="Shipping per warehouse",
        xlabel="Warehouse block",
        ylabel="Record count",
        color="tab:blue",
        fontsize=8
    )
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.savefig("docs/shipping_per_warehouse.png")
    
    # Grafica mode of shipment
    plt.figure()
    counts = data["Mode_of_Shipment"].value_counts()
    counts.plot.pie(
        title="Mode of shipment",
        wedgeprops=dict(width=0.35),
        ylabel="",
        colors=["tab:blue", "tab:orange", "tab:green"],
    )
    plt.savefig("docs/mode_of_shipment.png")

    # Grafica customer rating
    plt.figure()
    data = (data[["Mode_of_Shipment", "Customer_rating"]]
            .groupby("Mode_of_Shipment").describe())
    data.columns = data.columns.droplevel()
    data = data[["mean","min","max"]]
    plt.barh(
        y=data.index.values,
        width=data["max"].values -1,
        left=data["min"].values,
        height=0.9,
        color="lightgray",
        alpha=0.5
    )
    colors=["tab:green" if value>=3.0 else "tab:orange" for value in data["mean"].values]
    plt.barh(
        y=data.index.values,
        width=data["max"].values - 1,
        left=data["min"].values,
        height=0.5,
        color=colors,
        alpha=1.0
    )
    plt.title("Average customer rating")
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.gca().spines["left"].set_visible(False)
    plt.gca().spines["bottom"].set_visible(False)

    plt.savefig("docs/average_customer_rating.png")

    # Grafica weight distribution
    data=df.copy()
    plt.figure()
    data.Weight_in_gms.plot.hist(
        title="Shipping weight distribution",
        color="tab:orange",
        edgecolor="white",
    )
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.savefig("docs/weight_distribution.png")
    

    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """
pregunta_01()