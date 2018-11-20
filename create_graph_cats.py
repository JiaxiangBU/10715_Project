# Python
import wikipedia
from tqdm import tqdm
hop = 2
hop = input_dir = "wiki_graph/cat_edges%d.txt" % hop

if input_dir == "":
    edges = []
    seed_entities = [
        "beaver", "dolphin", "otter", "Pinniped", "whale","aquarium", "flatfish", "Batoidea", 
        "shark", "trout", "orchids", "poppy", "roses", "sunflowers", "tulips","bottles", 
        "bowls", "Aluminum_can", "cups", "Plate (dishware)", "apples", "mushrooms", "Orange (fruit)", "pears", 
        "Chili pepper","clock", "Computer keyboard", "Light_fixture", "telephone", "television", "bed", "chair", 
        "couch", "Table (furniture)", "wardrobe","bee", "beetle", "butterfly", "caterpillar", "cockroach",
        "bear", "leopard", "lion", "tiger", "wolf","bridge", "castle", "house", "road", "skyscraper",
        "cloud", "forest", "mountain", "plain", "sea","camel", "cattle", "chimpanzee", "elephant", 
        "kangaroo","fox", "porcupine", "Opossum", "raccoon", "skunk", "crab", "lobster", "snail", 
        "spider", "worm", "baby", "boy", "girl", "man", "woman", "crocodile", "dinosaur", "lizard", 
        "snake", "turtle", "hamster", "mouse", "rabbit", "shrew", "squirrel","maple", "oak", "Arecaceae", 
        "pine", "willow","bicycle", "bus", "motorcycle", "pickup_truck", "train","lawn_mower", "rocket", 
        "streetcar", "tank", "tractor"
    ]
    to_scrape = []
    for i, entity in enumerate(seed_entities):
        data = wikipedia.page(entity)
        print(i, data.title)
        cats = data.categories
        for cat in cats:
            if "wikipedia" in cat.lower():
                continue
            elif "articles" in cat.lower():
                continue
            elif "cs1" in cat.lower():
                continue
            elif "wikidata" in cat.lower():
                continue
            print((entity, cat))
            edges.append((entity, "Category:%s" % cat))
    output_file = open("wiki_graph/cat_edges.txt", "w")
    for edge in edges:
        output_file.write("%s\t%s\n" % (edge[0], edge[1]))
else:
    edges = []
    cats = []
    for line in open(input_dir):
        entity, cat = line.strip().split("\t")
        if "webarchive" in cat.lower():
            continue
        elif "pages" in cat.lower():
            continue
        edges.append((entity, cat))
        cats.append(cat)
    subcats = list(set(cats))
    for subcat in tqdm(subcats):
        try:
            data = wikipedia.page(subcat)
            supercats = data.categories
        except:
            continue
        for cat in supercats:
            if "wikipedia" in cat.lower():
                continue
            elif "articles" in cat.lower():
                continue
            elif "cs1" in cat.lower():
                continue
            elif "wikidata" in cat.lower():
                continue
            elif "webarchive" in cat.lower():
                continue
            edges.append((subcat, "Category:%s" % cat))
    output_file = open("wiki_graph/cat_edges%d.txt" % (hop + 1), "w")
    for edge in edges:
        output_file.write("%s\t%s\n" % (edge[0], edge[1]))