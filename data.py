
class_names = {
    # This was a syntax error. The string was broken into two lines.
    0: "Pepper bell Bacterial spot (alt)", # <-- FIX 2
    1: "Pepper bell healthy",
    2: "Potato Early blight",
    3: "Potato Late blight",
    4: "Potato healthy",
    5: "Tomato Bacterial spot",
    6: "Tomato Early blight",
    7: "Tomato Late blight",
    8: "Tomato Leaf Mold",
    9: "Tomato Septoria leaf spot",
    10: "Tomato Spider mites Two spotted spider mite",
    11: "Tomato Target_Spot",
    12: "Tomato YellowLeaf Curl Virus",
    13: "Tomato mosaic virus",
    14: "Tomato healthy",
}
remedies = {
    0: [
        "Remove and destroy infected plant parts.",
        "Apply copper-based fungicides or bactericides following label instructions.",
        "Rotate crops and practice good sanitation.",
    ],
    2: [
        "Remove and destroy infected leaves and plant debris.",
        "Apply fungicides containing chlorothalonil or copper-based fungicides following label instructions.",
        "Practice crop rotation and avoid overhead irrigation.",
    ],
    3: [
        "Remove and destroy infected plants and tubers.",
        "Apply fungicides containing chlorothalonil or copper-based fungicides following label instructions.",
        "Practice crop rotation and provide good airflow.",
    ],
    5: [
        "Remove and destroy infected plant parts.",
        "Apply copper-based bactericides following label instructions.",
        "Practice crop rotation and avoid overhead watering.",
    ],
    6: [
        "Remove and destroy infected leaves and plant debris.",
        "Apply fungicides containing chlorothalonil or copper-based fungicides following label instructions.",
        "Practice crop rotation, provide good airflow, and avoid overhead watering.",
    ],
    7: [
        "Remove and destroy infected plants and fruit.",
        "Apply fungicides containing chlorothalonil or copper-based fungicides following label instructions.",
        "Practice crop rotation, provide good airflow, and avoid overhead watering.",
    ],
    8: [
        "Remove and destroy infected leaves and plant debris.",
        "Provide good airflow and ventilation to reduce humidity.",
        "Avoid overhead watering and apply fungicides if necessary.",
    ],
    9: [
        "Remove and destroy infected leaves and plant debris.",
        "Apply fungicides containing chlorothalonil or copper-based fungicides following label instructions.",
        "Practice crop rotation, provide good airflow, and avoid overhead watering.",
    ],
    10: [
        "Spray affected plants with a strong jet of water to dislodge mites.",
        "Apply insecticidal soap or horticultural oil following label instructions.",
        "Introduce beneficial predatory mites or other natural enemies to control the population.",
    ],
    11: [
        "Remove and destroy infected leaves and plant debris.",
        "Apply fungicides containing chlorothalonil or copper-based fungicides following label instructions.",
        "Practice crop rotation, provide good airflow, and avoid overhead watering.",
    ],
    12: [
        "Plant resistant varieties if available.",
        "Control whiteflies, which spread the virus, using sticky traps or insecticides.",
        "Remove and destroy infected plants.",
    ],
    13: [
        "Plant resistant varieties if available.",
        "Control aphids, which transmit the virus, using insecticides or reflective mulches.",
        "Remove and destroy infected plants.",
    ],
}
# ... (your remedies dictionary ends here)
# ...

# --- NEW LIBRARY DATA ---
# We are manually structuring this for the frontend
# This makes it easy for the HTML to loop through
library_data = {
        "Tomato": [
        {
        "name": "Early Blight",
        "identification": [
            "Brown concentric ring spots on older leaves.",
            "Leaves yellow and drop prematurely.",
            "Fruit shows sunken, dark spots.",
            "Common in warm, humid weather."
        ],
        "remedy": [
            "Remove infected leaves.",
            "Avoid overhead irrigation.",
            "Apply fungicides like chlorothalonil or mancozeb.",
            "Practice crop rotation."
        ]
        },
        {
        "name": "Late Blight",
        "identification": [
            "Large irregular water-soaked lesions.",
            "White fungal growth under leaves in humidity.",
            "Fruit rot with firm brown patches.",
            "Spreads fast in cool, wet weather."
        ],
        "remedy": [
            "Destroy infected plants immediately.",
            "Improve field ventilation.",
            "Spray copper-based fungicides or metalaxyl.",
            "Avoid working with wet plants."
        ]
        },
        {
        "name": "Septoria Leaf Spot",
        "identification": [
            "Small circular spots with dark borders and gray centers.",
            "Lower leaves affected first.",
            "Leads to heavy defoliation.",
            "Occurs in warm and moist conditions."
        ],
        "remedy": [
            "Remove infected lower leaves.",
            "Mulch plants to prevent soil splash.",
            "Spray chlorothalonil or copper fungicides.",
            "Maintain adequate spacing."
        ]
        },
        {
        "name": "Bacterial Wilt",
        "identification": [
            "Sudden wilting of leaves without yellowing.",
            "Stem becomes slimy inside.",
            "White ooze comes out when cut and squeezed.",
            "Common in warm, moist soil."
        ],
        "remedy": [
            "Use resistant varieties.",
            "Remove and destroy infected plants.",
            "Improve soil drainage.",
            "Practice long-term crop rotation."
        ]
        },
        {
        "name": "Tomato Mosaic Virus (ToMV)",
        "identification": [
            "Mottling or mosaic yellow-green patterns.",
            "Distorted leaves with thin or curled edges.",
            "Reduced fruit size and yield.",
            "Transmitted through touch, tools and seeds."
        ],
        "remedy": [
            "Use certified virus-free seeds.",
            "Sanitize tools and hands regularly.",
            "Remove infected plants.",
            "Grow resistant varieties."
        ]
        }
    ],
    "Paddy": [
        {
        "name": "Bacterial Leaf Blight (BLB)",
        "identification": [
            "Yellowing and drying of leaf tips starting from margins.",
            "Water-soaked stripes that turn brown.",
            "Severe infection leads to 'kresek'—whole plant wilting.",
            "Occurs commonly after heavy rains or high nitrogen use."
        ],
        "remedy": [
            "Use resistant varieties (e.g., PTB33, IR64-BLB-resistant lines).",
            "Avoid excessive nitrogen fertilizer.",
            "Ensure proper field drainage.",
            "Spray copper oxychloride if infection is severe."
        ]
        },
        {
        "name": "Blast (Leaf, Node & Neck Blast)",
        "identification": [
            "Diamond-shaped gray lesions with brown borders on leaves.",
            "Blackening of nodes causing stem breakage.",
            "Neck infection leads to white, chaffy panicles.",
            "Occurs in cool, humid conditions."
        ],
        "remedy": [
            "Use resistant varieties.",
            "Avoid excessive nitrogen application.",
            "Maintain proper spacing to reduce humidity.",
            "Spray tricyclazole or isoprothiolane early."
        ]
        },
        {
        "name": "Sheath Blight",
        "identification": [
            "Oval-shaped lesions on leaf sheath.",
            "White fungal growth between tillers.",
            "Plants lodge due to weakened stems.",
            "High in dense, heavily fertilized fields."
        ],
        "remedy": [
            "Avoid dense planting.",
            "Apply potash-rich fertilizers.",
            "Remove infected stubbles.",
            "Spray validamycin or hexaconazole."
        ]
        },
        {
        "name": "Brown Spot",
        "identification": [
            "Brown circular spots with yellow halos on leaves.",
            "Reduces grain filling and plant vigor.",
            "Appears in nutrient-deficient or drought-stressed fields."
        ],
        "remedy": [
            "Use disease-free seeds.",
            "Apply potassium and phosphorus-based fertilizers.",
            "Improve soil fertility (especially zinc).",
            "Spray mancozeb or propiconazole."
        ]
        },
        {
        "name": "Rice Tungro Virus (RTV)",
        "identification": [
            "Yellow-orange discoloration of leaves.",
            "Stunted growth and reduced tillering.",
            "Shortened panicles with few grains.",
            "Spread by green leafhopper."
        ],
        "remedy": [
            "Grow resistant varieties.",
            "Control green leafhopper using recommended insecticides.",
            "Avoid staggered planting.",
            "Remove infected plants early."
        ]
        },
        {
        "name": "False Smut",
        "identification": [
            "Grains turn into yellow-green spore balls.",
            "Balls convert into orange or green velvety masses.",
            "Occurs in humid conditions during flowering."
        ],
        "remedy": [
            "Use certified seeds.",
            "Avoid excessive nitrogen.",
            "Spray carbendazim + mancozeb at booting stage.",
            "Maintain proper spacing."
        ]
        },
        {
        "name": "Sheath Rot",
        "identification": [
            "Brown, necrotic lesions on the sheath enclosing the panicle.",
            "Panicle emerges partially or poorly.",
            "Grains appear discolored or empty."
        ],
        "remedy": [
            "Use fungicide-treated seeds.",
            "Prevent lodging and leaf injury.",
            "Spray carbendazim or propiconazole."
        ]
        },
        {
        "name": "Stem Rot",
        "identification": [
            "Black lesions at the water line on stems.",
            "Hollow stem with fungal growth inside.",
            "Plants lodge and show stunted growth."
        ],
        "remedy": [
            "Avoid overuse of nitrogen.",
            "Practice crop rotation.",
            "Improve drainage.",
            "Spray validamycin or carbendazim."
        ]
        },
        {
        "name": "Bakanae Disease (Foot Rot)",
        "identification": [
            "Abnormally tall, thin, pale plants.",
            "Rotten lower stem and brown discoloration.",
            "Seedlings wilt and die."
        ],
        "remedy": [
            "Use hot-water-treated or fungicide-treated seeds.",
            "Avoid infected seed lots.",
            "Soak seeds in carbendazim solution."
        ]
        },
        {
        "name": "Narrow Brown Leaf Spot",
        "identification": [
            "Narrow, brown lesions along leaf veins.",
            "Severe infection leads to leaf drying.",
            "More common in older leaves."
        ],
        "remedy": [
            "Use resistant varieties.",
            "Spray mancozeb or tricyclazole.",
            "Maintain balanced nutrient levels."
        ]
        }
    ],

    "Wheat": [
        {
        "name": "Rust (Stem Rust / Leaf Rust / Stripe Rust)",
        "identification": [
            "Orange, brown, or yellow pustules depending on rust type.",
            "Occurs in stripes, random spots, or stems.",
            "Leaves dry prematurely.",
            "Favored by cool, moist weather."
        ],
        "remedy": [
            "Grow resistant varieties.",
            "Remove volunteer wheat plants.",
            "Spray propiconazole or tebuconazole.",
            "Avoid late sowing."
        ]
        },
        {
        "name": "Blight (Spot Blotch / Leaf Blight)",
        "identification": [
            "Dark brown irregular spots on leaves.",
            "Lesions expand and cause drying.",
            "Common in warm, humid areas."
        ],
        "remedy": [
            "Use disease-free seeds.",
            "Apply balanced nitrogen and potash.",
            "Use tolerant varieties.",
            "Spray mancozeb or propiconazole."
        ]
        },
        {
        "name": "Powdery Mildew",
        "identification": [
            "White powdery fungal growth on leaves and stems.",
            "Leaves curl and turn pale.",
            "Occurs in cool, dry climates."
        ],
        "remedy": [
            "Use resistant cultivars.",
            "Avoid excessive nitrogen.",
            "Provide proper spacing.",
            "Use sulfur dust or hexaconazole."
        ]
        },
        {
        "name": "Karnal Bunt",
        "identification": [
            "Black powdery fungal mass inside grains.",
            "Fishy odor from infected wheat.",
            "Partially infected grains appear shriveled."
        ],
        "remedy": [
            "Grow resistant varieties.",
            "Rotate crops.",
            "Treat seeds with carbendazim.",
            "Avoid late sowing."
        ]
        },
        {
        "name": "Loose Smut",
        "identification": [
            "Earheads converted into black spore masses.",
            "Entire spike replaced by dark powder.",
            "Spreads through infected seeds."
        ],
        "remedy": [
            "Use smut-free seeds.",
            "Hot water treatment (52°C for 10 min).",
            "Use systemic fungicides on seed."
        ]
        },
        {
        "name": "Seedling Blight",
        "identification": [
            "Poor germination or early seedling death.",
            "Brown discoloration at root or stem base.",
            "Seedlings appear weak and stunted."
        ],
        "remedy": [
            "Treat seeds with carbendazim or thiram.",
            "Avoid waterlogging.",
            "Maintain proper spacing."
        ]
        },
        {
        "name": "Fusarium Head Blight (Ear Blight)",
        "identification": [
            "Bleached spikelets with pink fungal growth.",
            "Shriveled grains (tombstone kernels).",
            "Occurs during humid flowering periods."
        ],
        "remedy": [
            "Practice crop rotation.",
            "Improve residue management.",
            "Spray tebuconazole at flowering.",
            "Avoid overhead irrigation."
        ]
        },
        {
        "name": "Root Rot / Foot Rot",
        "identification": [
            "Brown discoloration on roots and stem base.",
            "Plants show stunting and yellowing.",
            "Often due to poor drainage or monocropping."
        ],
        "remedy": [
            "Rotate with legumes.",
            "Improve soil drainage.",
            "Treat seeds with fungicides.",
            "Use organic matter to strengthen soil."
        ]
        },
        {
        "name": "Wheat Mosaic Virus",
        "identification": [
            "Yellow mosaic patterns on leaves.",
            "Stunted growth.",
            "Transmitted by soil-borne mites."
        ],
        "remedy": [
            "Use resistant varieties.",
            "Maintain field sanitation.",
            "Avoid early sowing in infected areas."
        ]
        },
        {
        "name": "Bacterial Leaf Streak",
        "identification": [
            "Water-soaked streaks that turn brown.",
            "Sticky bacterial ooze under humid conditions.",
            "Leaves shred and dry."
        ],
        "remedy": [
            "Use disease-free seeds.",
            "Avoid overhead irrigation.",
            "Improve field drainage.",
            "Spray copper-based bactericides."
        ]
        }
    ],
    "Potato": [
        {
        "name": "Late Blight",
        "identification": [
            "Water-soaked dark patches on leaves.",
            "White fungal growth on undersides.",
            "Dark brown, rotten tubers with smell.",
            "Spreads rapidly in cool, humid conditions."
        ],
        "remedy": [
            "Use blight-resistant varieties.",
            "Spray copper fungicides or metalaxyl.",
            "Improve drainage and avoid water stagnation.",
            "Destroy infected crop residues."
        ]
        },
        {
        "name": "Early Blight",
        "identification": [
            "Brown concentric ring spots on older leaves.",
            "Yellowing and drying of foliage.",
            "Reduced tuber development.",
            "Occurs in stressed plants or warm climates."
        ],
        "remedy": [
            "Apply mancozeb or chlorothalonil fungicides.",
            "Ensure balanced fertilization.",
            "Use disease-free seed tubers.",
            "Rotate crops for 2–3 years."
        ]
        },
        {
        "name": "Black Scurf (Rhizoctonia)",
        "identification": [
            "Black crust-like spots on tuber skin.",
            "Poor sprouting of seed potatoes.",
            "Stems show reddish-brown lesions.",
            "Emergence is delayed in infected fields."
        ],
        "remedy": [
            "Use certified seed tubers.",
            "Treat seeds with fungicides before planting.",
            "Avoid planting in cold or wet soils.",
            "Practice crop rotation."
        ]
        },
        {
        "name": "Potato Virus Y (PVY)",
        "identification": [
            "Mosaic patterns and leaf mottling.",
            "Stunted plants with reduced tuber size.",
            "Leaf curling and distortion.",
            "Transmitted by aphids."
        ],
        "remedy": [
            "Use virus-free seeds.",
            "Control aphids using recommended insecticides.",
            "Remove infected plants immediately.",
            "Grow resistant varieties."
        ]
        },
        {
        "name": "Common Scab",
        "identification": [
            "Rough corky lesions on tuber surface.",
            "Circular or irregular scabs.",
            "More severe in alkaline soils.",
            "Does not affect inside of tuber usually."
        ],
        "remedy": [
            "Maintain soil pH between 5.0–5.2.",
            "Use clean certified seed tubers.",
            "Avoid fresh manure before planting.",
            "Ensure proper irrigation during tuber formation."
        ]
        }
    ],

    "Bell Pepper": [
        {
        "name": "Anthracnose",
        "identification": [
            "Sunken dark lesions on fruits.",
            "Pinkish fungal ooze inside spots.",
            "Leaves develop small circular spots.",
            "Rapid spread during humid weather."
        ],
        "remedy": [
            "Use disease-free seeds.",
            "Remove infected fruits immediately.",
            "Spray fungicides such as carbendazim or mancozeb.",
            "Avoid overhead irrigation."
        ]
        },
        {
        "name": "Bacterial Leaf Spot",
        "identification": [
            "Small water-soaked spots that turn brown.",
            "Yellow halos around lesions.",
            "Severe leaf drop in infected plants.",
            "Spreads during rainfall or sprinklers."
        ],
        "remedy": [
            "Use copper-based bactericides.",
            "Avoid overhead watering.",
            "Use certified disease-free seeds.",
            "Rotate with non-host crops."
        ]
        },
        {
        "name": "Phytophthora Blight",
        "identification": [
            "Dark brown lesions at stem base.",
            "Sudden wilting of entire plant.",
            "Water-soaked fruit rot.",
            "Occurs in poorly drained fields."
        ],
        "remedy": [
            "Improve soil drainage.",
            "Apply metalaxyl or phosphonate fungicides.",
            "Raise beds for planting.",
            "Remove infected plants early."
        ]
        },
        {
        "name": "Powdery Mildew",
        "identification": [
            "White powdery fungus on leaves and stems.",
            "Leaves curl and turn yellow.",
            "Reduces fruit size.",
            "More common in dry, warm climates."
        ],
        "remedy": [
            "Improve air circulation.",
            "Avoid shading and overcrowding.",
            "Spray sulfur or potassium bicarbonate.",
            "Use resistant varieties if available."
        ]
        },
        {
        "name": "Bell Pepper Mosaic Virus",
        "identification": [
            "Light and dark green mottled patterns.",
            "Deformed leaves and shoestring appearance.",
            "Smaller fruits with rough surface.",
            "Spread by aphids and contaminated tools."
        ],
        "remedy": [
            "Remove infected plants.",
            "Control aphids with recommended insecticides.",
            "Use mosaic-resistant varieties.",
            "Sterilize tools regularly."
        ]
        }
    ]
    }