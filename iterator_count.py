import itertools

shipment_id_counter = itertools.count(start=1001, step=1)

def assign_shipment_id():
    return next(shipment_id_counter)

shipments = ['Shipment A', 'Shipment B', 'Shipment C']

for shipment in shipments:
    shipment_id = assign_shipment_id()
    print(f"{shipment} is assigned ID: {shipment_id}")
