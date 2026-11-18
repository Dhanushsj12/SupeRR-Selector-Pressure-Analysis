# 🏏 SupeRR Selector Season 2 · Round 1: Pressure Index
### *Who Delivers When the Match Is On the Line?*
**Author:** Dhanush S. J. (VIT Vellore)  
**Competition:** Rajasthan Royals – SupeRR Selector Season 2 (Round 1)  
**Dataset:** Supplied IPL + T20I ball-by-ball records, **2022–2026** (775 clean matches, 185,400 deliveries)

---

## 🌟 Executive Summary: Why This Approach Stands Apart

Most student entries in cricket analytics hackathons rely on **arbitrary rules of thumb**:
- Counting death overs (overs 16–20) as the only pressure situation.
- Ranking players by raw Strike Rate or Economy Rate, ignoring match context (e.g. chasing 220 vs defending 120).
- Hand-picking subjective formula weights (e.g. $0.4 \times \text{SR} + 0.3 \times \text{Dots} + \dots$).
- Allowing lucky small samples (a batter facing 10 balls and hitting two boundaries) to dominate leaderboards.

### Our Solution: A Standalone, Statistically Rigorous Framework
1. **Data-Derived Pressure (Leverage Index)**:
   - Pressure is defined strictly by **how much one ball can change the match win probability**.
   - Win probability is estimated via regularized logistic regression trained out-of-fold by match (Log-loss: Innings 1 = 0.633, Innings 2 = 0.411).
   - Leverage Index (LI) weights the 7 possible outcomes ($0, 1, 2, 3, 4, 6, \text{Wicket}$) by their empirical frequency in that match state.
   - The top 20% of leverage ($\text{LI} \ge 1.25$) defines **Pressure Balls**. Flagged balls carry **2.97 points of win-probability swing per ball** vs $1.00$ for ordinary balls, capturing **43% of all match swing in just 20% of deliveries**.
2. **Context-Matched Ball Valuation**:
   - Every delivery is evaluated using a non-linear expected remaining runs resource curve ($\text{ER} = a_w \cdot (1 - e^{-c_w \cdot \text{balls}})$) fitted per wickets lost.
   - Every ball is centered within its exact situation cell ($\text{pool} \times \text{innings} \times \text{phase} \times \text{wickets} \times \text{leverage decile}$). A player is only credited for beating what an *average player* produces in that exact spot.
3. **Empirical Bayes Shrinkage (DerSimonian–Laird)**:
   - Small samples are shrunk toward the population mean in proportion to match-clustered standard errors:
     $$\text{Shrunk} = \mu + B \cdot (\text{Observed} - \mu), \quad B = \frac{\tau^2}{\tau^2 + \text{SE}^2}$$
   - Prevents lucky small samples from topping the list while rewarding consistent high-sample performers.
4. **Interactive Executive Display Dashboard**:
   - A modern, interactive web application (`dashboard.html` / `app.py`) in Rajasthan Royals visual colors featuring top 10 cards, head-to-head radar scout tools, a live match leverage simulator, and empirical audit tables.

---

## 📋 Official Top 10 Rankings (For Unstop Dropdown Selection)

Enter these players in rank order from 1 to 10 on the Unstop submission dropdowns:

### Top 10 Batters Under Pressure
| Rank | Batter Name | Stability Tier | Pressure Balls | Matches | Predicted Level ($g+\delta$) | Consistency (Hit-Rate) | Final Clutch Score |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| **1** | **Suryakumar Yadav** | 🟢 Confirmed | 514 | 35 | **+25.42** | 23 / 35 (66%) | **25.92** |
| **2** | **Abhishek Sharma** | 🟢 Confirmed | 428 | 35 | **+25.07** | 21 / 35 (60%) | **25.31** |
| **3** | **Phil Salt** | 🟢 Confirmed | 260 | 21 | **+22.12** | 14 / 21 (67%) | **22.50** |
| **4** | **Tim David** | 🟢 Confirmed | 275 | 25 | **+21.64** | 13 / 25 (52%) | **21.58** |
| **5** | **Heinrich Klaasen** | 🟢 Confirmed | 231 | 18 | **+20.02** | 12 / 18 (67%) | **20.36** |
| **6** | **Vaibhav Sooryavanshi** | 🟢 Confirmed | 140 | 14 | **+18.53** | 9 / 14 (64%) | **18.75** |
| **7** | **Mitchell Marsh** | 🟡 Probable | 433 | 29 | **+18.43** | 18 / 29 (62%) | **18.73** |
| **8** | **Travis Head** | 🟡 Probable | 217 | 19 | **+15.81** | 13 / 19 (68%) | **16.22** |
| **9** | **Namboori Tilak Varma** | 🟡 Probable | 573 | 33 | **+14.52** | 17 / 33 (52%) | **14.42** |
| **10** | **Reeza Hendricks** | 🔴 Toss-up | 169 | 10 | **+13.89** | 7 / 10 (70%) | **14.17** |

*Reserves (Next in line):* Muhammad Waseem, Nicholas Pooran, David Warner.

---

### Top 10 Bowlers Under Pressure
| Rank | Bowler Name | Stability Tier | Pressure Balls | Matches | Predicted Level ($g+\delta$) | Consistency (Hit-Rate) | Final Clutch Score |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| **1** | **Sunil Narine** | 🟢 Confirmed | 322 | 23 | **+20.49** | 17 / 23 (74%) | **23.01** |
| **2** | **Rashid Khan** | 🟢 Confirmed | 439 | 31 | **+16.58** | 21 / 31 (68%) | **18.66** |
| **3** | **Jasprit Bumrah** | 🟢 Confirmed | 325 | 26 | **+14.42** | 15 / 26 (58%) | **15.28** |
| **4** | **Kuldeep Yadav** | 🟢 Confirmed | 314 | 23 | **+12.32** | 17 / 23 (74%) | **14.83** |
| **5** | **Axar Patel** | 🟡 Probable | 394 | 32 | **+9.36** | 21 / 32 (66%) | **11.21** |
| **6** | **Varun Chakravarthy** | 🟡 Probable | 381 | 28 | **+9.56** | 15 / 28 (54%) | **10.05** |
| **7** | **Krunal Pandya** | 🟡 Probable | 280 | 20 | **+8.45** | 12 / 20 (60%) | **9.38** |
| **8** | **Nathan Ellis** | 🟡 Probable | 203 | 12 | **+8.27** | 8 / 12 (67%) | **9.36** |
| **9** | **Mitchell Santner** | 🟡 Probable | 295 | 29 | **+7.95** | 18 / 29 (62%) | **9.31** |
| **10** | **Bhuvneshwar Kumar** | 🟡 Probable | 502 | 35 | **+8.84** | 18 / 35 (51%) | **9.16** |

*Reserves (Next in line):* Wanindu Hasaranga, Abrar Ahmed, Blessing Muzarabani.

*(Note: Places 5–10 for bowlers are near-ties, appearing in the top 10 in 42%–60% of random 80% resamples).*

---

## 🔬 Data Accounting & Exclusions (100% Verified)

- **Total matches listed:** 883 matches.
- **Matches with ball-by-ball delivery records:** 867 matches.
- **Matches used in rating pipeline:** **775 clean matches** (IPL 355 · T20I 420).
- **Matches excluded:** **92 matches**:
  - **T20I Excluded (50 matches):** 29 rain-revised (DLS), 19 abandoned / no result, 2 incomplete.
  - **IPL Excluded (12 matches):** 6 rain-revised (DLS), 5 abandoned / no result, 1 incomplete.
  - **Non-Target Competitions Excluded (30 matches):** Other tournament matches (e.g. WPL) outside the IPL & Men's T20I scope.
- **Deliveries modeled:** 185,400 balls.

---

## 📊 Matched Head-to-Head Out-of-Sample Proof (Zero Data Leakage)

In rigorous audit testing, our leverage model was compared against an industry-standard **Percentile Composite Benchmark** (combining strike-rate / economy, survival / wicket rates, and consistency) and a **Usual-Level-Only Baseline** across 12 random half-splits:

| Evaluation Scope | Held-out Target | Our Leverage Model | Percentile Composite | Usual Level Only | Verdict |
|:---|:---|:---:|:---:|:---:|:---|
| **Batters (Not Nested)** | Pressure Value ($\Delta$ Runs) | **0.273** | 0.156 | 0.264 | **+75% ahead of rule composite** |
| **Batters (Fully Nested)** | Pressure Value ($\Delta$ Runs) | **0.119** | 0.052 | 0.160 | **More than double rule composite** |
| **Batters (Fully Nested)** | Rule-Flag Strike Rate | **0.160** | 0.103 | **0.274** | Usual level is strongest predictor |
| **Bowlers (Not Nested)** | Pressure Value ($\Delta$ Runs) | **0.275** | 0.147 | 0.266 | **+87% ahead of rule composite** |
| **Bowlers (Fully Nested)** | Pressure Value ($\Delta$ Runs) | **0.207** | 0.141 | 0.171 | **Clear leader on value** |
| **Bowlers (Fully Nested)** | Rule-Flag −Economy | **0.302** | 0.274 | 0.298 | **Beats both benchmarks** |

*Core Insight:* Predicting clutch performance is predominantly predicting overall player quality ($g$), with a modest pressure deviation ($\delta$). Our model consistently beats rule composites without leakage.

---

## 🚀 How to Run the Code & Launch the Interactive App

### 1. Open the Interactive Web Dashboard (Zero Setup)
Simply double-click `dashboard.html` or `index.html` in your browser! It runs fully offline with zero server dependencies, providing:
- Interactive Leaderboard cards with tier filters and Unstop copy button.
- Multidimensional Radar Chart comparing any two players side-by-side.
- Live Win-Probability & Match Leverage Simulator with adjustable sliders.
- Audit & validation tables.

### 2. Launch the Local Flask Web Server
To launch the live web application with REST API:
```bash
python app.py --port 5000
```
Open [http://localhost:5000](http://localhost:5000) in your browser.

### 3. Run the Entire Analytics Pipeline from Scratch
To execute the entire pipeline end-to-end, update all CSVs, regenerate figures, recompile Jupyter notebooks, and refresh dashboard data:
```bash
python run_pipeline.py --fast     # Evaluation run (~3-4 min)
python run_pipeline.py --full     # Full production run (60 subsamples, ~15 min)
```

### 4. Run Individual Notebooks
Each stage is cleanly packaged into an executable, documented Jupyter notebook:
1. `08_player_ranking.ipynb` – Data cleaning, Win-prob model, Leverage Index, Empirical Bayes ratings.
2. `10_extra_validation.ipynb` – Season stakes simulation, signal persistence, tournament of variants, confidence tiers.
3. `11_audit_tests.ipynb` – Matched head-to-head nested cross-validation, sensitivity checks.

---

## 📁 Repository Structure
```
d:\ipl_player_display/
├── Data Pack/                         # Supplied competition CSVs
│   ├── ball_by_ball.csv
│   ├── matches.csv
│   ├── competitions.csv
│   ├── teams.csv
│   └── playing_eleven.csv
├── outputs/                           # Generated results
│   ├── player_ranking/
│   │   ├── top10_batters.csv          # Official Unstop Batters Submission
│   │   ├── top10_bowlers.csv          # Official Unstop Bowlers Submission
│   │   ├── full_ratings_bat.csv       # All 91 eligible batters
│   │   ├── full_ratings_bowl.csv      # All 98 eligible bowlers
│   │   ├── fig_top10.png              # Top 10 bar chart with 80% CI
│   │   └── fig_leverage_by_over.png   # Leverage curve by over
│   ├── extra_validation/
│   │   ├── confidence_tiers_bat.csv   # Batter tiers & resample stability
│   │   ├── confidence_tiers_bowl.csv  # Bowler tiers & resample stability
│   │   ├── season_stakes.csv          # Monte Carlo playoff race stakes
│   │   └── variant_tournament.csv     # Model tournament results
│   └── audit/
│       ├── matched_head_to_head.csv   # Nested cross-validation results
│       └── sensitivity_variants.csv   # Illegal balls & threshold checks
├── dashboard.html                     # Standalone Interactive Web Dashboard (offline ready)
├── index.html                         # Root entry for static hosting
├── app.py                             # Flask Web Server & REST API
├── build_dashboard.py                 # Dashboard builder script
├── generate_dashboard_data.py         # Data aggregator for dashboard
├── run_pipeline.py                    # Master orchestrator script
├── pressure_pipeline.py               # Main ranking pipeline script
├── extra_validation.py                # Validation and tiers script
├── audit_tests.py                     # Audit tests script
├── convert.py                         # Python to Jupyter Notebook compiler
├── 08_player_ranking.ipynb            # Interactive Notebook 1
├── 10_extra_validation.ipynb          # Interactive Notebook 2
├── 11_audit_tests.ipynb               # Interactive Notebook 3
├── presentation.pptx                  # PowerPoint presentation (2022–2026 verified)
├── METHODOLOGY.md                     # Comprehensive technical documentation
└── README.md                          # Executive project documentation
```

---

## 🏆 Key Conclusions for Rajasthan Royals Scouting
- **Batters:** Suryakumar Yadav and Abhishek Sharma form an elite tier (+25 runs/100 balls above average under pressure), followed by Phil Salt, Tim David, Heinrich Klaasen, and 14-year-old phenom Vaibhav Sooryavanshi (+18.5).
- **Bowlers:** Sunil Narine (+20.5) and Rashid Khan (+16.6) lead world cricket in pressure containment, with Jasprit Bumrah (+14.4) and Kuldeep Yadav (+12.3) rounding out the confirmed core.
- **Scouting Realism:** Players deliver under pressure primarily because of extraordinary baseline skill that does not collapse when the match is on the line. Small sample size claims of an isolated "clutch gene" fail out-of-sample tests; what counts is high baseline reliability, which our framework isolates and proves.
