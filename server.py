from email.mime import image
from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
import json, random
app = Flask(__name__)

beans = {
    "1":{
        "id": "1",
        "name": "Guatemala El Socorro Gesha Coe #2",
        "image": "https://cdn.shopify.com/s/files/1/1707/3261/products/ColombiaTioConejoGesha_c5562c47-3e0f-40a2-94fe-066a6cfe6785_1200x.png?v=1629213154",
        "roaster" : "Oynx",
        "variety": ["Gesha"],
        "process": ["Washed", "Raised Bed Dried"],
        "elevation": 1859,
        "roast": "Medium Light",
        "notes": ["Jasmine", "Raw Sugar", "Milk Tea", "Pineapple"],
        "description": "With this beautiful washed Gesha, Juan Colom of El Socorro secured the number two spot in the Cup of Excellence. This washed microlot is the near perfect expression of Gesha, with stunning floral notes, balanced out by delicate tropical fruits and a rich raw sugar sweetness."
	},
    "2":{
        "id": "2",
        "name": "Colombia Double Fermented Gesha - 2nd Anniversary",
        "image": "https://cdn.shopify.com/s/files/1/1995/6387/products/pair_cupworks_62_doublefermentedgesha_2890x.jpg?v=1645465497",
        "roaster" : "Pair Cupworks",
        "variety": ["Gesha"],
        "process": ["Double Fermentation", "Aerobic", "Anaerobic"],
        "elevation": 1460,
        "roast": "Medium Light",
        "notes": ["Strawberry", "Vanilla", "Bananas Foster"],
        "description": "It’s a celebration! This gesha varietal coffee is grown by El Vergel Farm and double fermented by producers Elias and Shady Bayter, located in Tolima, Colombia. In celebration of our cafe's 2nd anniversary, we are happy to present this super limited release! Cheers! Don't be intimidated by this coffee -- it is extremely forgiving to brew! A light roast level preserves the beautiful fruity and floral qualities of the varietal, while the extra fermentation processing creates more permeability which helps offset the difficulties usually associated with brewing light-roast coffees."
    },
    "3":{
        "id": "3",
        "name": "Colombia Rubiela Velazquez",
        "image": "https://cdn.shopify.com/s/files/1/0002/6352/0281/products/Rubiela_2560x.png?v=1645664310",
        "roaster" : "Sey",
        "variety": ["Castillo Tambo"],
        "process": ["Washed", "Raised Bed Dried"],
        "elevation": 1900,
        "roast": "Light",
        "notes": ["Dark Fruit", "Yellow Tropicals", "Excellent Sweetness"],
        "description": "Rubiela has been working with our exporting partner Alejandro Renjifo for many years. She is an extremely dedicated and talented producer, and a cornerstone of the specialty coffee growing community of Tolima. We've tasted her coffees year after year for as long as we've been working in Colombia, and we continue to look forward to tasting them each season. Rubiela has a very long history of producing beautiful coffees, and this lovely Castillo Tambo is no exception. In the cup we find dark fruit, yellow tropicals, and excellent sweetness."
    },
    "4":{
        "id": "4",
        "name": "Wild Forest",
        "image": "https://cdn.shopify.com/s/files/1/0734/9587/products/WILDFORESTUSProductShotBags_800x.png?v=1612898836",
        "roaster" : "Devoción",
        "variety": ["Caturra"],
        "process": ["Washed"],
        "elevation": 1750,
        "roast": "Light",
        "notes": ["Wild Berries", "Cherry", "Agraz (Andean Blueberry)", "Cocoa Butter", "Caramel"],
        "description": "When we use the phrase ‘Active Harvest’ to refer to the regions of our House Blends, we’re referring to Colombian growing regions that are currently harvesting coffee at the time of sourcing. Only buying coffee from farms located in active harvest regions, and never using warehoused beans or third-party importers, allows us to guarantee that 100% of our coffee, not just limited editions but even our House Blends, are roasted while still fresh, 365 days a year. "
    },
    "5":{
        "id": "5",
        "name": "Honduras Fredy Sabillon - Parainema Honey",
        "image": "https://cdn.shopify.com/s/files/1/2988/2574/products/fredyhoney_cardonline_1_22_3x-100_1800x1800.jpg?v=1641409331",
        "roaster" : "Black & White",
        "variety": ["Parainema"],
        "process": ["Honey"],
        "elevation": 1350,
        "roast": "Light Medium",
        "notes": ["Tangerine", "White Wine", "Blondie"],
        "description": "Fredy Sabillon's Honey process Parainema is brought to us with the help of Benjamin. Fredy and his brother have owned their farm since 2006 and have been producing specialty coffee since 2018. The unique variety they grow, Parainema, is the result of breeding the Villa Sarchi and Timor varieties. The variety was developed with resistance to coffee leaf rust in mind. The variety is relatively large and quite dense with a very impressive cup quality (most coffees bred for leaf rust resistance are not known to be particularly tasty). In 2017, a Parainema variety coffee won the Honduras Cup of Excellence, cementing its fame as a delicious variety. This Honey process coffee tastes like ripe tangerines and bright, white wine. We also taste baked chocolate complimented with a creamy mouthfeel that reminds us of a warm blondie."  
    },
    "6":{
        "id": "6",
        "name": "Colombia Ivan Molano",
        "image": "https://cdn.shopify.com/s/files/1/0002/6352/0281/products/pulgas_2560x.png?v=1582103690",
        "roaster" : "Sey",
        "variety": ["Caturra"],
        "process": ["Washed"],
        "elevation": 2070,
        "roast": "Light",
        "notes": ["Chocolate", "Red Fruit", "Subtle Acidity"],
        "description": "This is our fourth year working with Ivan Molano. Ivan is a true coffee producer; his family has been producing coffee for many generations—longer than any of them can remember. Ivan inherited his 11 hectare (~27 acres) farm from his father, and has dedicated himself to maximizing quality. He believes doing so is the best way to make a living for his family, and  also best for the future of coffee production for his children. His farm, Las Pulgas, rests at the top of the mountains in Planadas. It enjoys warm days and cold nights, which is perfect for slow and even cherry maturation. We are very happy to continue working with this beautiful coffee from this dedicated family."
    },
    "7":{
        "id": "7",
        "name": "Costa Rica Las Lajas SL28 Natural",
        "image": "https://cdn.shopify.com/s/files/1/1707/3261/products/CostaRicaLasLajasSL28Natural.png?v=1644960155",
        "roaster" : "Oynx",
        "variety": ["SL-28"],
        "process": ["Natural", "Patio Dried"],
        "elevation": 1450,
        "roast": "Light",
        "notes": ["Raspberry", "Grapefruit", "Cola", "Thick"],
        "description": "Our third and final release from the talented farm Las Lajas is this special honey processed SL28 variety. Usually grown in East Africa (Kenya specifically), this variety yields large amounts of naturally occurring phosphoric acid. This comes across as a tactile feel rather than a flavor. A mouthwatering, juicy texture that lights up the palate. This coffee is one of a kind and won’t last long."
    },
    "8":{
        "id": "8",
        "name": "Carbonic Maceration Processed Coffee Beans from Ethiopia",
        "image": "https://cdn.shopify.com/s/files/1/1995/6387/products/pair_cupworks_XX_carbonic_ethiopia4_2890x.jpg?v=1641190685",
        "roaster" : "Pair Cupworks",
        "variety": ["Ethiopia Landraces"],
        "process": ["Carbonic Maceration"],
        "elevation": 2200,
        "roast": "Light",
        "notes": ["Pinot", "Honey", "Blueberry"],
        "description": "This coffee takes all the marbles, sweet, fruity, yet sophisticated! Grown by various smallholder farms, processed at the Dumerso Washing Station using cold and controlled carbonic fermentation. This coffee is tasty any way you brew it, but we've been especially loving it brewed with a 1:15 ratio, full-immersion on the Hario Switch or Clever brewer, bringing out the sweetness with a slightly fuller body -- delicious!"
    },
    "9":{
        "id": "9",
        "name": "Colombia Juan Jimenez",
        "image": "https://cdn.shopify.com/s/files/1/1707/3261/products/ColombiaJuanJimenez_9bd65849-8c7c-4e30-aed2-f2c35caf8664.png?v=1639071756",
        "roaster" : "Oynx",
        "variety": ["Pink Bourbon"],
        "process": ["Washed", "Raised-Bed Dried"],
        "elevation": 1700,
        "roast": "Light",
        "notes": ["Confectioners Sugar", "Black Tea", "Honeysuckle", "Melon"],
        "description": "This unique coffee comes from southern Huila, from Juan Jimenez. Sr. Jimenez grows Caturra, Colombia, and Pink Bourbon on his 16 hectare farm. Each variety is meticulously picked and processed with quality in mind. Both Juan and his wife Leidy manage the farm, taking care to reinvest earnings into the farm each harvest in order to sustain high quality harvests for years to come. Kyle at Osito has been working with El Porvenir for two years, buying a large amount of all the varieties produced on their farm. This season was marks our second year purchasing not only Juan’s pink bourbon, but his caturra as well."
    },
    "10":{
        "id": "10",
        "name": "La Mandarina - Women In Coffee",
        "image": "https://cdn.shopify.com/s/files/1/0734/9587/products/LamandarinaproductshotINGLES_800x.png?v=1646006112",
        "roaster" : "Devoción",
        "variety": ["Castillo", "Típica"],
        "process": ["N/A"],
        "elevation": 1750,
        "roast": "Medium Light",
        "notes": ["Stonefruit", "Panela", "Vanilla"],
        "description": "The Típica trees on producer Martha Obando’s farm have been around longer than she’s been alive. The delicious coffee they produce is common to the region, which is experiencing a revitalization after years of armed conflict. Obando’s role as a leader of the ASOFINCAS association, entrepreneur and mother has contributed to this turnaround, helping people learn more about growing high-quality coffee and, in turn, helping them earn more money for the product they produce."
    }
}

# ROUTES
@app.route('/')
def display_home():
    beanList = random.sample(list(beans.values()), 6)
    return render_template('home.html', beans=beanList)  

@app.route('/view/<id>')
def view(id=None):
    global beans
    bean = beans[id]
    return render_template('view.html', bean=bean)

@app.route('/edit_bean/<id>')
def edit_bean(id=None):
    global beans
    bean = beans[id]
    return render_template('edit.html', bean=bean)

@app.route('/add_bean')
def add_bean():
    global beans
    bean = beans["3"]
    return render_template('add.html', bean=bean)

@app.route('/post_add/<id>')
def post_add(id=None):
    global beans
    bean = beans[id]
    return render_template('post_add.html', bean=bean)

# AJAX FUNCTIONS

@app.route('/search_results/<search_text>')
def search_results(search_text=None):
    global beans
    result_count = 0
    new_search_text = search_text.lower()
    results = [[],[],[]]
    fields = ["name", "roaster", "description"]
    for bean in beans.values():
        bean_name = bean["name"].lower()
        bean_roaster = bean["roaster"].lower()
        bean_description = bean["description"].lower()
        if new_search_text in bean_name:
            results[0].append(bean)
            result_count += 1 
        if new_search_text in bean_roaster:
            results[1].append(bean)
            result_count += 1 
        if new_search_text in bean_description:
            results[2].append(bean)
            result_count += 1 
    
    return render_template('search_results.html', search_text = search_text, results = results, fields = fields, count=result_count)


@app.route('/add_entry', methods=['GET', 'POST'])
def add_entry():
    global beans
    json_data = request.get_json()
    
    id = str(len(beans) + 1)   
    name = json_data["name"] 
    image = json_data["image"]
    roaster = json_data["roaster"]
    variety = json_data["variety"]
    process = json_data["process"]
    elevation = json_data["elevation"]
    roast = json_data["roast"]
    notes = json_data["notes"]
    description = json_data["description"]

    new_entry = {
        "id": id,
        "name": name,
        "image": image,
        "roaster": roaster,
        "variety": variety,
        "process": process,
        "elevation": elevation,
        "roast": roast,
        "notes": notes,
        "description": description
    }

    beans[id] = new_entry
    print("add bean success")

    return jsonify(id = id)


@app.route('/edit_entry', methods=['GET', 'POST'])
def edit_entry():
    global beans
    json_data = request.get_json()
    
    id = json_data["id"] 
    name = json_data["name"] 
    image = json_data["image"]
    roaster = json_data["roaster"]
    variety = json_data["variety"]
    process = json_data["process"]
    elevation = json_data["elevation"]
    roast = json_data["roast"]
    notes = json_data["notes"]
    description = json_data["description"]

    edited_entry = {
        "id": id,
        "name": name,
        "image": image,
        "roaster": roaster,
        "variety": variety,
        "process": process,
        "elevation": elevation,
        "roast": roast,
        "notes": notes,
        "description": description
    }

    beans[id] = edited_entry
    print("edit bean success")
    
    return jsonify(id = id)


if __name__ == '__main__':
   app.run(debug = True)
