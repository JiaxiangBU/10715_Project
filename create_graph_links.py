# Python
import wikipedia
from tqdm import tqdm

hop = 1
input_dir = ""

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
        links = data.links
        for dest in links:
            print((entity, dest))
            edges.append((entity, dest))
    output_file = open("wiki_graph/edges1.txt", "w")
    for edge in edges:
        output_file.write("%s\t%s\n" % (edge[0], edge[1]))
