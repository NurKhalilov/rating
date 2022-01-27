from .models import Rating
import pandas as pd
import json
import matplotlib.pyplot as plt
import base64
from io import BytesIO


def json_maker():
    rating = Rating.objects.all()
    json_data = []
    for rate in rating:
        data = {
            "id": rate.id,
            "salesperson": rate.salesperson.name,
            "rating": rate.rating,
            "sent_time": rate.sent_time.strftime("%d/%m/%Y %H:%M:%S"),
        }
        json_data.append(data)
    return json.dumps(json_data, indent=4, sort_keys=True, default=str)


def average_values():
    average_values_in_json = []
    data = json_maker()
    df = pd.read_json(data)
    df = df.set_index('id')
    salesman_group = df.groupby(['salesperson'])
    for person in df['salesperson'].unique():
        salesperson = salesman_group.get_group(f"{person}").mean().round(2)
        data = {
            "salesperson": person,
            "average": salesperson['rating']
        }
        average_values_in_json.append(data)
    return average_values_in_json
    

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph
    

def get_plot(x, y, z):
    
    plt.style.use('seaborn')
    plt.switch_backend('AGG')
    fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)
    ax1.bar(x, y)
    for i in range(len(x)):
        ax1.text(i, y[i], str(y[i]), ha="center", va="bottom")
    ax1.set_title("Sotuvchilarning o'rtacha baholari", pad=20)
    ax1.set_xlabel('Sotuvchining ismi', fontsize=16)
    ax1.set_ylabel('Baho', fontsize=16)

    ax2.bar(x, z, color='#00FF00')
    for i in range(len(z)):
        ax2.text(i, y[i], str(z[i]))
    ax2.set_title("Umumiy ko'rsatilgan xizmatlar soni", pad=20)
    ax2.set_xlabel('Sotuvchining ismi', fontsize=16)
    ax2.set_ylabel('Soni', fontsize=16)
    
    plt.tight_layout()
    graph = get_graph()
    return graph
