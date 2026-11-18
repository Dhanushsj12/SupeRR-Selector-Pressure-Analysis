import os
import json
import pandas as pd
import numpy as np

# Detailed metadata for cricketers
PLAYER_PROFILE_META = {
    # Batters
    "Suryakumar Yadav": {
        "short_name": "SKY",
        "team": "MI",
        "country": "India",
        "flag": "🇮🇳",
        "jersey": "63",
        "rating": 98,
        "title": "360° MR. CLUTCH",
        "img": "https://documents.iplt20.com/ipl/IPLHeadshot2024/174.png",
        "backup_img": "https://img1.hscicdn.com/image/upload/f_auto,t_ds_square_w_320,q_50/lsci/db/PICTURES/CMS/388900/388941.1.png"
    },
    "Abhishek Sharma": {
        "short_name": "ABHI",
        "team": "SRH",
        "country": "India",
        "flag": "🇮🇳",
        "jersey": "4",
        "rating": 97,
        "title": "FEARLESS POWER STRIKER",
        "img": "https://documents.iplt20.com/ipl/IPLHeadshot2024/1113.png",
        "backup_img": "https://a.espncdn.com/combiner/i?img=/i/headshots/cricket/players/full/1070183.png"
    },
    "Phil Salt": {
        "short_name": "SALT",
        "team": "KKR",
        "country": "England",
        "flag": "🏴󠁧󠁢󠁥󠁮󠁧󠁿",
        "jersey": "28",
        "rating": 95,
        "title": "HIGH-LEVERAGE BLITZER",
        "img": "https://documents.iplt20.com/ipl/IPLHeadshot2024/1187.png",
        "backup_img": "https://a.espncdn.com/combiner/i?img=/i/headshots/cricket/players/full/643907.png"
    },
    "Tim David": {
        "short_name": "DAVID",
        "team": "MI",
        "country": "Australia",
        "flag": "🇦🇺",
        "jersey": "8",
        "rating": 94,
        "title": "DEATH-OVER FINISHER",
        "img": "https://documents.iplt20.com/ipl/IPLHeadshot2024/4524.png",
        "backup_img": "https://a.espncdn.com/combiner/i?img=/i/headshots/cricket/players/full/892749.png"
    },
    "Heinrich Klaasen": {
        "short_name": "KLAAS",
        "team": "SRH",
        "country": "South Africa",
        "flag": "🇿🇦",
        "jersey": "45",
        "rating": 94,
        "title": "SPIN & PACE PUNISHER",
        "img": "https://documents.iplt20.com/ipl/IPLHeadshot2024/202.png",
        "backup_img": "https://a.espncdn.com/combiner/i?img=/i/headshots/cricket/players/full/438691.png"
    },
    "Vaibhav Sooryavanshi": {
        "short_name": "VAIBH",
        "team": "RR",
        "country": "India",
        "flag": "🇮🇳",
        "jersey": "13",
        "rating": 93,
        "title": "14-YR PHENOM DISRUPTOR",
        "img": "https://img1.hscicdn.com/image/upload/f_auto,t_ds_square_w_320,q_50/lsci/db/PICTURES/CMS/388900/388941.1.png",
        "backup_img": "https://images.firstpost.com/uploads/2024/11/Vaibhav-Suryavanshi-2024-11-209a80b852932c0d024626156e7dfbf3.jpg"
    },
    "Mitchell Marsh": {
        "short_name": "MARSH",
        "team": "DC",
        "country": "Australia",
        "flag": "🇦🇺",
        "jersey": "8",
        "rating": 92,
        "title": "PRESSURE POWER ANCHOR",
        "img": "https://documents.iplt20.com/ipl/IPLHeadshot2024/40.png",
        "backup_img": "https://a.espncdn.com/combiner/i?img=/i/headshots/cricket/players/full/272450.png"
    },
    "Travis Head": {
        "short_name": "HEAD",
        "team": "SRH",
        "country": "Australia",
        "flag": "🇦🇺",
        "jersey": "62",
        "rating": 91,
        "title": "POWERPLAY ASSAILANT",
        "img": "https://documents.iplt20.com/ipl/IPLHeadshot2024/1020.png",
        "backup_img": "https://a.espncdn.com/combiner/i?img=/i/headshots/cricket/players/full/530011.png"
    },
    "Namboori Tilak Varma": {
        "short_name": "TILAK",
        "team": "MI",
        "country": "India",
        "flag": "🇮🇳",
        "jersey": "9",
        "rating": 90,
        "title": "CALCULATED RESCUE ENGINE",
        "img": "https://documents.iplt20.com/ipl/IPLHeadshot2024/993.png",
        "backup_img": "https://a.espncdn.com/combiner/i?img=/i/headshots/cricket/players/full/1170265.png"
    },
    "Reeza Hendricks": {
        "short_name": "HENDR",
        "team": "SA",
        "country": "South Africa",
        "flag": "🇿🇦",
        "jersey": "17",
        "rating": 89,
        "title": "TARGET CHASE SPEARHEAD",
        "img": "https://img1.hscicdn.com/image/upload/f_auto,t_ds_square_w_320,q_50/lsci/db/PICTURES/CMS/319700/319746.png",
        "backup_img": "https://a.espncdn.com/combiner/i?img=/i/headshots/cricket/players/full/269280.png"
    },
    "Virat Kohli": {
        "short_name": "VK",
        "team": "RCB",
        "country": "India",
        "flag": "🇮🇳",
        "jersey": "18",
        "rating": 88,
        "title": "CHASE MASTER ANCHOR",
        "img": "https://documents.iplt20.com/ipl/IPLHeadshot2024/2.png",
        "backup_img": "https://a.espncdn.com/combiner/i?img=/i/headshots/cricket/players/full/253802.png"
    },
    "Nicholas Pooran": {
        "short_name": "POORAN",
        "team": "LSG",
        "country": "West Indies",
        "flag": "🏝️",
        "jersey": "29",
        "rating": 90,
        "title": "MAXIMUM BOUNDARY SURGE",
        "img": "https://documents.iplt20.com/ipl/IPLHeadshot2024/136.png",
        "backup_img": "https://a.espncdn.com/combiner/i?img=/i/headshots/cricket/players/full/604302.png"
    },
    "David Warner": {
        "short_name": "WARNER",
        "team": "DC",
        "country": "Australia",
        "flag": "🇦🇺",
        "jersey": "31",
        "rating": 89,
        "title": "AGGRESSIVE VETERAN LEAD",
        "img": "https://documents.iplt20.com/ipl/IPLHeadshot2024/170.png",
        "backup_img": "https://a.espncdn.com/combiner/i?img=/i/headshots/cricket/players/full/219889.png"
    },

    # Bowlers
    "Sunil Narine": {
        "short_name": "NARIN",
        "team": "KKR",
        "country": "West Indies",
        "flag": "🏝️",
        "jersey": "74",
        "rating": 99,
        "title": "MYSTERY DEFENSIVE APEX",
        "img": "https://documents.iplt20.com/ipl/IPLHeadshot2024/156.png",
        "backup_img": "https://a.espncdn.com/combiner/i?img=/i/headshots/cricket/players/full/230558.png"
    },
    "Rashid Khan": {
        "short_name": "RASHD",
        "team": "GT",
        "country": "Afghanistan",
        "flag": "🇦🇫",
        "jersey": "19",
        "rating": 97,
        "title": "GLOBAL T20 STRIKE KING",
        "img": "https://documents.iplt20.com/ipl/IPLHeadshot2024/218.png",
        "backup_img": "https://a.espncdn.com/combiner/i?img=/i/headshots/cricket/players/full/793463.png"
    },
    "Jasprit Bumrah": {
        "short_name": "BUMRH",
        "team": "MI",
        "country": "India",
        "flag": "🇮🇳",
        "jersey": "93",
        "rating": 97,
        "title": "YORKER & DEATH FORTRESS",
        "img": "https://documents.iplt20.com/ipl/IPLHeadshot2024/9.png",
        "backup_img": "https://a.espncdn.com/combiner/i?img=/i/headshots/cricket/players/full/625383.png"
    },
    "Kuldeep Yadav": {
        "short_name": "KULDP",
        "team": "DC",
        "country": "India",
        "flag": "🇮🇳",
        "jersey": "23",
        "rating": 94,
        "title": "CLUTCH DRIFT MAGICIAN",
        "img": "https://documents.iplt20.com/ipl/IPLHeadshot2024/14.png",
        "backup_img": "https://a.espncdn.com/combiner/i?img=/i/headshots/cricket/players/full/559241.png"
    },
    "Axar Patel": {
        "short_name": "AXAR",
        "team": "DC",
        "country": "India",
        "flag": "🇮🇳",
        "jersey": "20",
        "rating": 92,
        "title": "PINPOINT CHOKE ARTIST",
        "img": "https://documents.iplt20.com/ipl/IPLHeadshot2024/110.png",
        "backup_img": "https://a.espncdn.com/combiner/i?img=/i/headshots/cricket/players/full/554618.png"
    },
    "Varun Chakravarthy": {
        "short_name": "VARUN",
        "team": "KKR",
        "country": "India",
        "flag": "🇮🇳",
        "jersey": "29",
        "rating": 91,
        "title": "MIDDLE-OVER ENIGMA",
        "img": "https://documents.iplt20.com/ipl/IPLHeadshot2024/140.png",
        "backup_img": "https://a.espncdn.com/combiner/i?img=/i/headshots/cricket/players/full/1157978.png"
    },
    "Krunal Pandya": {
        "short_name": "KRUNL",
        "team": "LSG",
        "country": "India",
        "flag": "🇮🇳",
        "jersey": "24",
        "rating": 90,
        "title": "TACTICAL TIGHT-LINE SPECIALIST",
        "img": "https://documents.iplt20.com/ipl/IPLHeadshot2024/17.png",
        "backup_img": "https://a.espncdn.com/combiner/i?img=/i/headshots/cricket/players/full/471342.png"
    },
    "Nathan Ellis": {
        "short_name": "ELLIS",
        "team": "PBKS",
        "country": "Australia",
        "flag": "🇦🇺",
        "jersey": "12",
        "rating": 90,
        "title": "DEATH-OVER CHANGEUP ACE",
        "img": "https://documents.iplt20.com/ipl/IPLHeadshot2024/764.png",
        "backup_img": "https://a.espncdn.com/combiner/i?img=/i/headshots/cricket/players/full/825075.png"
    },
    "Mitchell Santner": {
        "short_name": "SANTN",
        "team": "CSK",
        "country": "New Zealand",
        "flag": "🇳🇿",
        "jersey": "77",
        "rating": 89,
        "title": "PRESSURE FLAT-ARC CHOKE",
        "img": "https://documents.iplt20.com/ipl/IPLHeadshot2024/190.png",
        "backup_img": "https://a.espncdn.com/combiner/i?img=/i/headshots/cricket/players/full/502714.png"
    },
    "Bhuvneshwar Kumar": {
        "short_name": "BHUVI",
        "team": "SRH",
        "country": "India",
        "flag": "🇮🇳",
        "jersey": "15",
        "rating": 89,
        "title": "VETERAN SWING & DEATH EXEC",
        "img": "https://documents.iplt20.com/ipl/IPLHeadshot2024/15.png",
        "backup_img": "https://a.espncdn.com/combiner/i?img=/i/headshots/cricket/players/full/326016.png"
    },
    "Wanindu Hasaranga": {
        "short_name": "HASAR",
        "team": "SRH",
        "country": "Sri Lanka",
        "flag": "🇱🇰",
        "jersey": "49",
        "rating": 89,
        "title": "MIDDLE WRIST-SPIN FORCE",
        "img": "https://documents.iplt20.com/ipl/IPLHeadshot2024/377.png",
        "backup_img": "https://a.espncdn.com/combiner/i?img=/i/headshots/cricket/players/full/784379.png"
    },
    "Patrick Cummins": {
        "short_name": "CUMMN",
        "team": "SRH",
        "country": "Australia",
        "flag": "🇦🇺",
        "jersey": "30",
        "rating": 88,
        "title": "PACE LEADER & SKIPPER",
        "img": "https://documents.iplt20.com/ipl/IPLHeadshot2024/33.png",
        "backup_img": "https://a.espncdn.com/combiner/i?img=/i/headshots/cricket/players/full/489889.png"
    }
}

# The 17 retained players requested for the RR roster panel. The photo URLs
# point to IPL / franchise / ICC / cricket-board player portraits.
RR_RETAINED_PLAYERS = [
    ("Riyan Parag", "https://documents.iplt20.com/ipl/IPLHeadshot2026/1005.png"),
    ("Yashasvi Jaiswal", "https://documents.iplt20.com/ipl/IPLHeadshot2026/533.png"),
    ("Vaibhav Sooryavanshi", "https://documents.iplt20.com/ipl/IPLHeadshot2026/3498.png"),
    ("Ravindra Jadeja", "https://images.icc-cricket.com/image/upload/t_player-headshot-portrait-lg-webp/prd/assets/players/8322/3850.png"),
    ("Dhruv Jurel", "https://documents.iplt20.com/ipl/IPLHeadshot2026/1004.png"),
    ("Jofra Archer", "https://documents.iplt20.com/ipl/IPLHeadshot2026/181.png"),
    ("Aman Rao Perala", "https://images.mykhel.com/webp/common_dynamic/images/auction_players/AMAN_RAO_PERALA_02062004.jpg"),
    ("Brijesh Sharma", "https://m.economictimes.com/thumb/msid-129903911,width-1200,height-1200,resizemode-4,imgsize-17742/brijesh-sharma-ipl-rajasthan-royals.jpg"),
    ("Nandre Burger", "https://www.rajasthanroyals.com/static-assets/images/players/66195.png?v=7.86"),
    ("Dasun Shanaka", "https://wisden.com/static-assets/images/players/59067.png?v=23.72"),
    ("Donovan Ferreira", "https://www.rajasthanroyals.com/static-assets/images/players/23487.png?v=7.76"),
    ("Lhuan-dre Pretorius", "https://documents.iplt20.com/ipl/IPLHeadshot2026/2827.png"),
    ("Ravi Bishnoi", "https://documents.iplt20.com/ipl/IPLHeadshot2026/520.png"),
    ("Sandeep Sharma", "https://documents.iplt20.com/ipl/IPLHeadshot2026/220.png"),
    ("Shubham Dubey", "https://static.toiimg.com/photo/120897495.cms"),
    ("Sushant Mishra", "https://www.rajasthanroyals.com/static-assets/images/players/71380.png?v=7.44"),
    ("Yash Punja", "https://documents.iplt20.com/ipl/IPLHeadshot2026/4553.png"),
]
RR_RELEASED_PLAYERS = ["Tushar Deshpande", "Adam Milne", "Kuldeep Sen", "Yudhvir Singh Charak", "Kwena Maphaka", "Vignesh Puthur", "Shimron Hetmyer", "Ravi Singh", "Emanjot Singh Chahal"]
RR_MOVED_PLAYERS = [
    {"name":"Sam Curran", "status":"Traded to Lucknow Super Giants"},
    {"name":"Mohammed Shami", "status":"Traded in from Lucknow Super Giants"},
    {"name":"Manimaran Siddharth", "status":"Traded in from Lucknow Super Giants"},
]

# Current team tags and fresh portrait URLs for the requested players.
PLAYER_PROFILE_META["Phil Salt"].update({"team":"RCB", "img":"https://img1.hscicdn.com/image/upload/f_auto%2Ct_ds_square_w_640%2Cq_50/lsci/db/PICTURES/CMS/383100/383141.png", "backup_img":"https://a.espncdn.com/combiner/i?img=/i/headshots/cricket/players/full/643907.png"})
PLAYER_PROFILE_META["Tim David"].update({"team":"RCB", "img":"https://static-files.cricket-australia.pulselive.com/headshots/440/3619-camedia.png", "backup_img":"https://a.espncdn.com/combiner/i?img=/i/headshots/cricket/players/full/892749.png"})
PLAYER_PROFILE_META["Mitchell Marsh"].update({"team":"LSG", "img":"https://images.icc-cricket.com/image/upload/t_player-headshot-portrait-lg-webp/prd/assets/players/13203/10094.png", "backup_img":"https://a.espncdn.com/combiner/i?img=/i/headshots/cricket/players/full/272450.png"})
PLAYER_PROFILE_META["Vaibhav Sooryavanshi"].update({"img":"https://documents.iplt20.com/ipl/IPLHeadshot2026/3498.png", "backup_img":"https://static.toiimg.com/photo/120728679.cms"})
PLAYER_PROFILE_META["Abhishek Sharma"].update({"img":"https://documents.iplt20.com/ipl/IPLHeadshot2026/212.png?v=3.19", "backup_img":"https://a.espncdn.com/combiner/i?img=/i/headshots/cricket/players/full/1070183.png"})
PLAYER_PROFILE_META["Namboori Tilak Varma"].update({"img":"https://documents.iplt20.com/ipl/IPLHeadshot2024/993.png", "backup_img":"https://a.espncdn.com/combiner/i?img=/i/headshots/cricket/players/full/1170265.png"})
PLAYER_PROFILE_META["Reeza Hendricks"].update({"img":"https://static-files.cricket-australia.pulselive.com/headshots/440/669-camedia.png", "backup_img":"https://a.espncdn.com/combiner/i?img=/i/headshots/cricket/players/full/269280.png"})
PLAYER_PROFILE_META["Nathan Ellis"].update({"img":"https://www.wisden.com/static-assets/images/players/70324.png?v=23.35", "backup_img":"https://a.espncdn.com/combiner/i?img=/i/headshots/cricket/players/full/825075.png"})
PLAYER_PROFILE_META["Krunal Pandya"].update({"team":"RCB", "img":"https://www.wisden.com/static-assets/images/players/63788.png?v=23.65", "backup_img":"https://a.espncdn.com/combiner/i?img=/i/headshots/cricket/players/full/471342.png"})
PLAYER_PROFILE_META["Bhuvneshwar Kumar"].update({"team":"RCB", "img":"https://www.iplt20.com/_next/image?q=75&url=%2Fapi%2Fteam-assets%3Fpathname%3Dplayer%252F8903%252F2138%252F12690.png%26brand%3Dipl&w=750", "backup_img":"https://a.espncdn.com/combiner/i?img=/i/headshots/cricket/players/full/326016.png"})
PLAYER_PROFILE_META["Kuldeep Yadav"].update({"team":"LSG", "img":"https://a.espncdn.com/combiner/i?img=/i/headshots/cricket/players/full/559241.png", "backup_img":"https://documents.iplt20.com/ipl/IPLHeadshot2024/14.png"})

def build_dashboard_data():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    pr_dir = os.path.join(base_dir, "outputs", "player_ranking")
    ev_dir = os.path.join(base_dir, "outputs", "extra_validation")
    au_dir = os.path.join(base_dir, "outputs", "audit")

    top_bat = pd.read_csv(os.path.join(pr_dir, "top10_batters.csv"))
    top_bowl = pd.read_csv(os.path.join(pr_dir, "top10_bowlers.csv"))

    tiers_bat = pd.read_csv(os.path.join(ev_dir, "confidence_tiers_bat.csv"))
    tiers_bowl = pd.read_csv(os.path.join(ev_dir, "confidence_tiers_bowl.csv"))

    full_bat = pd.read_csv(os.path.join(pr_dir, "full_ratings_bat.csv"))
    full_bowl = pd.read_csv(os.path.join(pr_dir, "full_ratings_bowl.csv"))

    tb_map = tiers_bat.set_index("name")["tier"].to_dict()
    tb_var_map = tiers_bat.set_index("name")["variants_top10"].to_dict()
    tb_sub_map = tiers_bat.set_index("name")["top10_given_eligible"].to_dict()

    tbowl_map = tiers_bowl.set_index("name")["tier"].to_dict()
    tbowl_var_map = tiers_bowl.set_index("name")["variants_top10"].to_dict()
    tbowl_sub_map = tiers_bowl.set_index("name")["top10_given_eligible"].to_dict()

    # Enrich full ratings
    full_bat["tier"] = full_bat["name"].map(tb_map).fillna("Unranked")
    full_bat["variants_top10"] = full_bat["name"].map(tb_var_map).fillna(0.0)
    full_bat["resamples_top10"] = full_bat["name"].map(tb_sub_map).fillna(0.0)

    full_bowl["tier"] = full_bowl["name"].map(tbowl_map).fillna("Unranked")
    full_bowl["variants_top10"] = full_bowl["name"].map(tbowl_var_map).fillna(0.0)
    full_bowl["resamples_top10"] = full_bowl["name"].map(tbowl_sub_map).fillna(0.0)

    top_bat["tier"] = top_bat["name"].map(tb_map).fillna("Toss-up")
    top_bat["variants_top10"] = top_bat["name"].map(tb_var_map).fillna(0.0)
    top_bat["resamples_top10"] = top_bat["name"].map(tb_sub_map).fillna(0.0)

    top_bowl["tier"] = top_bowl["name"].map(tbowl_map).fillna("Toss-up")
    top_bowl["variants_top10"] = top_bowl["name"].map(tbowl_var_map).fillna(0.0)
    top_bowl["resamples_top10"] = top_bowl["name"].map(tbowl_sub_map).fillna(0.0)

    # Load module breakdowns
    try:
        chase_bat = pd.read_csv(os.path.join(pr_dir, "module_chase_bat.csv")).set_index("name")
        chase_bowl = pd.read_csv(os.path.join(pr_dir, "module_chase_bowl.csv")).set_index("name")
    except Exception:
        chase_bat, chase_bowl = pd.DataFrame(), pd.DataFrame()

    try:
        ko_bat = pd.read_csv(os.path.join(pr_dir, "module_knockout_bat.csv")).set_index("name")
        ko_bowl = pd.read_csv(os.path.join(pr_dir, "module_knockout_bowl.csv")).set_index("name")
    except Exception:
        ko_bat, ko_bowl = pd.DataFrame(), pd.DataFrame()

    try:
        ls_bat = pd.read_csv(os.path.join(pr_dir, "module_longshot_bat.csv")).set_index("name")
        ls_bowl = pd.read_csv(os.path.join(pr_dir, "module_longshot_bowl.csv")).set_index("name")
    except Exception:
        ls_bat, ls_bowl = pd.DataFrame(), pd.DataFrame()

    try:
        buildup = pd.read_csv(os.path.join(pr_dir, "module_buildup_pressure.csv")).to_dict(orient="records")
    except Exception:
        buildup = []

    try:
        defs_comp = pd.read_csv(os.path.join(pr_dir, "pressure_definition_comparison.csv")).to_dict(orient="records")
    except Exception:
        defs_comp = []

    try:
        matched_h2h = pd.read_csv(os.path.join(au_dir, "matched_head_to_head.csv")).to_dict(orient="records")
    except Exception:
        matched_h2h = []

    try:
        sensitivity = pd.read_csv(os.path.join(au_dir, "sensitivity_variants.csv")).to_dict(orient="records")
    except Exception:
        sensitivity = []

    # Helper to add situational profiles and face card assets
    def enrich_players(df, role):
        records = []
        for _, r in df.iterrows():
            nm = r["name"]
            c_val = chase_bat.loc[nm, "level"] if (role == "bat" and nm in chase_bat.index) else (
                    chase_bowl.loc[nm, "level"] if (role == "bowl" and nm in chase_bowl.index) else None)
            k_diff = ko_bat.loc[nm, "diff"] if (role == "bat" and nm in ko_bat.index) else (
                     ko_bowl.loc[nm, "diff"] if (role == "bowl" and nm in ko_bowl.index) else None)
            ls_val = ls_bat.loc[nm, "level"] if (role == "bat" and nm in ls_bat.index) else (
                     ls_bowl.loc[nm, "level"] if (role == "bowl" and nm in ls_bowl.index) else None)

            rec = r.to_dict()
            rec["chase_level"] = round(float(c_val), 2) if c_val is not None and not np.isnan(c_val) else None
            rec["ko_diff"] = round(float(k_diff), 2) if k_diff is not None and not np.isnan(k_diff) else None
            rec["longshot_level"] = round(float(ls_val), 2) if ls_val is not None and not np.isnan(ls_val) else None

            # Add face card meta
            meta = PLAYER_PROFILE_META.get(nm, {
                "short_name": nm.split()[-1][:5].upper(),
                "team": "T20",
                "country": "International",
                "flag": "🏏",
                "jersey": "00",
                "rating": max(85, int(95 - rec.get("rank", 20))),
                "title": "CLUTCH PERFORMER",
                "img": f"https://api.dicebear.com/7.x/bottts/svg?seed={nm}",
                "backup_img": f"https://api.dicebear.com/7.x/identicon/svg?seed={nm}"
            })
            rec.update(meta)
            records.append(rec)
        return records

    batters_all_list = enrich_players(full_bat, "bat")
    bowlers_all_list = enrich_players(full_bowl, "bowl")

    # Also enrich top10 lists
    top_bat_enriched = [b for b in batters_all_list if b["rank"] <= 10]
    top_bowl_enriched = [b for b in bowlers_all_list if b["rank"] <= 10]

    data = {
        "metadata": {
            "title": "Rajasthan Royals SupeRR Selector · Season 2 · Round 1",
            "subtitle": "Who Delivers When the Match Is On the Line? Leverage-Based Pressure Ranking",
            "author": "Dhanush S. J. (VIT Vellore)",
            "scope": "IPL + T20I (2022–2026)",
            "matches_total": 883,
            "matches_ball_by_ball": 867,
            "matches_used": 775,
            "matches_excluded": 92,
            "exclusion_breakdown": {
                "t20i_excluded": 50,
                "ipl_excluded": 12,
                "other_competitions_excluded": 30
            },
            "balls_analyzed": 185400,
            "pressure_threshold": "Top 20% Leverage Index (LI >= 1.25)",
            "swing_captured_pct": 43.0,
            "swing_per_pressure_ball": 2.97,
            "swing_per_ordinary_ball": 1.00,
            "batters_eligible": len(full_bat),
            "bowlers_eligible": len(full_bowl)
        },
        "top10_batters": top_bat_enriched,
        "top10_bowlers": top_bowl_enriched,
        "all_batters": batters_all_list,
        "all_bowlers": bowlers_all_list,
        "rr_retained_players": [
            {"name": name, "team":"RR", "status":"Retained", "captain": name == "Riyan Parag", "img": image}
            for name, image in RR_RETAINED_PLAYERS
        ],
        "rr_released_players": RR_RELEASED_PLAYERS,
        "rr_moved_players": RR_MOVED_PLAYERS,
        "pressure_definitions": defs_comp,
        "buildup_pressure": buildup,
        "matched_head_to_head": matched_h2h,
        "sensitivity": sensitivity
    }

    out_file = os.path.join(base_dir, "dashboard_data.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"Wrote enriched dashboard data to {out_file} ({len(batters_all_list)} batters, {len(bowlers_all_list)} bowlers)")
    return data

if __name__ == "__main__":
    build_dashboard_data()
