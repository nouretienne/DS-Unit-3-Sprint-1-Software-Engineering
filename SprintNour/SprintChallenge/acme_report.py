from acme import Product

adj = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
name = ['Anvil', 'Catapult','Disguise', 'Mousetrap', '???']

def generate_products(time=30):
       li = []
    for i in range(time):
        li.append(Product(random.choice(adj) + ' ' + random.choice(name)))
        li[i].price = random.randint(50,100)
        li[i].weight = random.randint(50,100)
        li[i].flammability = random.uniform(0.0, 2.5)
    return li  

def inventory_report(li):
    name_list = []
    mean_price = 0
    mean_weight = 0
    mean_flammability = 0
    for j in range(len(li)):
        name_list.append(li[j].name)
        mean_price += li[j].price
        mean_weight += li[j].weight
        mean_flammability += li[j].flammability
    price_mean = mean_price/len(li)
    weight_mean = mean_weight/len(li)
    flammability_mean = mean_flammability/len(li)
    unique_names_list = []  
    for x in name_list:  
        if x not in unique_names_list: 
            unique_names_list.append(x)
    print('The number of unique products in the list is ',len(unique_names_list))
    print('The average mean price is', price_mean)
    print('The average mean weight is', weight_mean)
    print('The average mean flammability is', flammability_mean)

if __name__ == '__main__':
    inventory_report(generate_products())

