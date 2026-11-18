import json
import os

def create_dashboard_html():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base_dir, "dashboard_data.json")
    with open(json_path, "r", encoding="utf-8") as f:
        data_json_str = f.read()

    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rajasthan Royals · SupeRR Selector S2 · Pressure Index & Cricketer Cards</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --rr-pink: #E41C6A;
            --rr-pink-light: #FF2E7E;
            --rr-pink-glow: rgba(228, 28, 106, 0.35);
            --rr-navy: #001D48;
            --rr-navy-deep: #000F26;
            --rr-navy-surface: #07224F;
            --rr-navy-border: rgba(255, 255, 255, 0.1);
            --rr-gold: #FFD700;
            --rr-gold-glow: rgba(255, 215, 0, 0.3);
            --rr-cyan: #00E5FF;
            --rr-emerald: #10B981;
            --rr-amber: #F59E0B;
            --text-main: #FFFFFF;
            --text-muted: #94A3B8;
            --text-dim: #64748B;
            --card-bg: rgba(7, 34, 79, 0.75);
            --card-hover: rgba(12, 45, 102, 0.9);
            --glass-border: 1px solid rgba(255, 255, 255, 0.1);
            --radius-lg: 18px;
            --radius-md: 12px;
            --radius-sm: 6px;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Outfit', 'Inter', -apple-system, sans-serif;
        }}

        body {{
            background: radial-gradient(circle at 15% 15%, #001A3F 0%, #000F26 50%, #000714 100%);
            color: var(--text-main);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            overflow-x: hidden;
        }}

        /* Header Navigation */
        header {{
            background: rgba(0, 15, 38, 0.9);
            backdrop-filter: blur(18px);
            border-bottom: 1px solid rgba(228, 28, 106, 0.35);
            position: sticky;
            top: 0;
            z-index: 100;
            padding: 0.85rem 2rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}

        .brand-area {{
            display: flex;
            align-items: center;
            gap: 1rem;
        }}

        .rr-logo-badge {{
            width: 46px;
            height: 46px;
            border-radius: 13px;
            background: linear-gradient(135deg, var(--rr-pink), #9B073D);
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 900;
            font-size: 1.45rem;
            color: #FFF;
            box-shadow: 0 4px 20px var(--rr-pink-glow);
            border: 1px solid rgba(255, 255, 255, 0.25);
        }}

        .brand-text h1 {{
            font-size: 1.3rem;
            font-weight: 900;
            letter-spacing: -0.5px;
            background: linear-gradient(90deg, #FFFFFF, #FFD700);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}

        .brand-text p {{
            font-size: 0.78rem;
            color: var(--text-muted);
            letter-spacing: 0.2px;
        }}

        .nav-tabs {{
            display: flex;
            gap: 0.5rem;
            background: rgba(255, 255, 255, 0.04);
            padding: 0.3rem;
            border-radius: 12px;
            border: var(--glass-border);
        }}

        .nav-btn {{
            background: transparent;
            border: none;
            color: var(--text-muted);
            padding: 0.5rem 1.15rem;
            border-radius: 9px;
            font-size: 0.88rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s ease;
            display: flex;
            align-items: center;
            gap: 0.4rem;
        }}

        .nav-btn:hover {{
            color: #FFF;
            background: rgba(255, 255, 255, 0.06);
        }}

        .nav-btn.active {{
            background: var(--rr-pink);
            color: #FFF;
            box-shadow: 0 2px 14px var(--rr-pink-glow);
        }}

        /* Hero Banner */
        .hero-banner {{
            padding: 2.2rem 2rem 1.2rem;
            max-width: 1440px;
            margin: 0 auto;
            width: 100%;
        }}

        .hero-grid {{
            display: grid;
            grid-template-columns: 2fr 1fr;
            gap: 1.8rem;
            align-items: center;
        }}

        .hero-title-area h2 {{
            font-size: 2.5rem;
            font-weight: 900;
            line-height: 1.15;
            letter-spacing: -1px;
            margin-bottom: 0.75rem;
        }}

        .hero-title-area h2 span.gradient {{
            background: linear-gradient(135deg, #FF2E7E 0%, #FFD700 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}

        .hero-subtitle {{
            font-size: 0.98rem;
            color: #CBD5E1;
            line-height: 1.55;
            max-width: 720px;
            margin-bottom: 1.2rem;
        }}

        .pill-row {{
            display: flex;
            flex-wrap: wrap;
            gap: 0.6rem;
        }}

        .badge-pill {{
            background: rgba(255, 255, 255, 0.06);
            border: 1px solid rgba(255, 255, 255, 0.12);
            padding: 0.35rem 0.85rem;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: 600;
            color: #E2E8F0;
            display: flex;
            align-items: center;
            gap: 0.4rem;
        }}

        .badge-pill.pink {{
            border-color: rgba(228, 28, 106, 0.5);
            background: rgba(228, 28, 106, 0.12);
            color: #FF75A9;
        }}

        .badge-pill.gold {{
            border-color: rgba(255, 215, 0, 0.5);
            background: rgba(255, 215, 0, 0.1);
            color: #FFE566;
        }}

        /* Hero Quick Stats */
        .stat-cards-trio {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 0.9rem;
        }}

        .stat-card-mini {{
            background: var(--card-bg);
            border: var(--glass-border);
            border-radius: var(--radius-md);
            padding: 1.15rem;
            text-align: center;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
            transition: transform 0.2s;
        }}

        .stat-card-mini:hover {{
            transform: translateY(-2px);
            border-color: rgba(228, 28, 106, 0.45);
        }}

        .stat-card-mini .val {{
            font-size: 1.85rem;
            font-weight: 900;
            color: #FFF;
            line-height: 1.1;
        }}

        .stat-card-mini .lbl {{
            font-size: 0.72rem;
            color: var(--text-muted);
            margin-top: 0.35rem;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            font-weight: 700;
        }}

        /* Main Container */
        main {{
            max-width: 1440px;
            margin: 0 auto;
            width: 100%;
            padding: 1rem 2rem 3rem;
            flex: 1;
        }}

        .tab-section {{
            display: none;
            animation: fadeIn 0.25s ease-in-out;
        }}

        .tab-section.active {{
            display: block;
        }}

        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(6px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        /* Section Headers */
        .section-header {{
            display: flex;
            justify-content: space-between;
            align-items: flex-end;
            margin-bottom: 1.4rem;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            padding-bottom: 0.8rem;
        }}

        .section-title h3 {{
            font-size: 1.55rem;
            font-weight: 800;
            letter-spacing: -0.5px;
            display: flex;
            align-items: center;
            gap: 0.6rem;
        }}

        .section-title p {{
            font-size: 0.88rem;
            color: var(--text-muted);
            margin-top: 0.2rem;
        }}

        /* Role Switcher */
        .role-switcher {{
            display: flex;
            background: rgba(0, 0, 0, 0.3);
            padding: 0.25rem;
            border-radius: 10px;
            border: var(--glass-border);
        }}

        .role-btn {{
            background: transparent;
            border: none;
            color: var(--text-muted);
            padding: 0.45rem 1.25rem;
            border-radius: 8px;
            font-size: 0.88rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s;
        }}

        .role-btn.active {{
            background: var(--rr-pink);
            color: #FFF;
            box-shadow: 0 2px 10px var(--rr-pink-glow);
        }}

        /* ============================================================== */
        /* CRICKETER ULTIMATE TEAM FACE CARD GRID                         */
        /* ============================================================== */
        .cards-grid-super {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(330px, 1fr));
            gap: 1.4rem;
            margin-bottom: 2.2rem;
        }}

        .cricketer-card {{
            background: linear-gradient(155deg, rgba(8, 32, 74, 0.85) 0%, rgba(3, 18, 46, 0.95) 100%);
            border: 1px solid rgba(255, 255, 255, 0.12);
            border-radius: var(--radius-lg);
            overflow: hidden;
            position: relative;
            transition: all 0.3s cubic-bezier(0.165, 0.84, 0.44, 1);
            display: flex;
            flex-direction: column;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
            cursor: pointer;
        }}

        .cricketer-card:hover {{
            transform: translateY(-6px);
            border-color: rgba(228, 28, 106, 0.6);
            box-shadow: 0 16px 45px rgba(228, 28, 106, 0.25);
        }}

        .cricketer-card.rank-1 {{
            border: 2px solid var(--rr-gold);
            background: linear-gradient(155deg, rgba(30, 22, 60, 0.9) 0%, rgba(10, 16, 40, 0.95) 100%);
            box-shadow: 0 10px 40px var(--rr-gold-glow);
        }}

        .cricketer-card.rank-1::before {{
            content: "👑 RANK #1 CLUTCH KING";
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            background: linear-gradient(90deg, #FFD700, #FFA500);
            color: #000;
            font-size: 0.68rem;
            font-weight: 900;
            letter-spacing: 0.8px;
            padding: 0.25rem 0;
            text-align: center;
            z-index: 10;
        }}

        /* Face Card Visual Stage */
        .card-stage {{
            position: relative;
            height: 190px;
            background: radial-gradient(circle at 50% 30%, rgba(228, 28, 106, 0.25) 0%, rgba(0, 0, 0, 0) 70%);
            display: flex;
            align-items: flex-end;
            justify-content: center;
            padding-bottom: 0.5rem;
            overflow: hidden;
            isolation: isolate;
        }}

        .cricketer-card.rank-1 .card-stage {{
            background: radial-gradient(circle at 50% 30%, rgba(255, 215, 0, 0.25) 0%, rgba(0, 0, 0, 0) 70%);
        }}

        /* Holographic Card Badges Overlay */
        .card-overlay-badge-left {{
            position: absolute;
            top: 14px;
            left: 14px;
            display: flex;
            flex-direction: column;
            align-items: center;
            z-index: 5;
        }}

        .cricketer-card.rank-1 .card-overlay-badge-left {{
            top: 26px;
        }}

        .ovr-box {{
            font-size: 1.85rem;
            font-weight: 900;
            line-height: 1;
            color: #FFF;
            text-shadow: 0 2px 10px rgba(0,0,0,0.5);
        }}

        .cricketer-card.rank-1 .ovr-box {{
            color: var(--rr-gold);
        }}

        .ovr-lbl {{
            font-size: 0.62rem;
            font-weight: 800;
            color: var(--rr-pink-light);
            letter-spacing: 0.5px;
        }}

        .cricketer-card.rank-1 .ovr-lbl {{
            color: var(--rr-gold);
        }}

        .team-pill {{
            background: rgba(0, 0, 0, 0.5);
            border: 1px solid rgba(255, 255, 255, 0.2);
            padding: 0.15rem 0.45rem;
            border-radius: 4px;
            font-size: 0.68rem;
            font-weight: 800;
            color: #FFF;
            margin-top: 0.35rem;
        }}

        .country-flag {{
            font-size: 1.25rem;
            margin-top: 0.25rem;
        }}

        /* Rank Badge Right */
        .card-overlay-badge-right {{
            position: absolute;
            top: 14px;
            right: 14px;
            z-index: 5;
            display: flex;
            flex-direction: column;
            align-items: flex-end;
            gap: 0.4rem;
        }}

        .cricketer-card.rank-1 .card-overlay-badge-right {{
            top: 26px;
        }}

        .rank-tag-large {{
            background: rgba(0, 0, 0, 0.6);
            border: 1px solid rgba(255, 255, 255, 0.2);
            font-size: 0.85rem;
            font-weight: 900;
            padding: 0.2rem 0.6rem;
            border-radius: 8px;
            color: #FFF;
        }}

        .cricketer-card.rank-1 .rank-tag-large {{
            background: var(--rr-gold);
            color: #000;
            border-color: #FFF;
        }}

        /* Player Face Photo */
        .player-headshot-img {{
            width: min(58%, 210px);
            height: 100%;
            max-height: 178px;
            object-fit: contain;
            object-position: center bottom;
            padding: 8px 0 0;
            box-sizing: border-box;
            filter: drop-shadow(0 8px 16px rgba(0, 0, 0, 0.6));
            transition: transform 0.3s ease;
            z-index: 2;
        }}

        .cricketer-card:hover .player-headshot-img {{
            transform: scale(1.05);
        }}

        /* Card Content Area */
        .card-content {{
            padding: 1.1rem 1.3rem 1.3rem;
            background: rgba(0, 15, 38, 0.6);
            border-top: 1px solid rgba(255, 255, 255, 0.08);
            display: flex;
            flex-direction: column;
            flex: 1;
            justify-content: space-between;
        }}

        .player-name-title-row {{
            margin-bottom: 0.9rem;
        }}

        .player-spec-banner {{
            font-size: 0.68rem;
            font-weight: 800;
            color: var(--rr-pink-light);
            letter-spacing: 0.8px;
            text-transform: uppercase;
            margin-bottom: 0.2rem;
        }}

        .cricketer-card.rank-1 .player-spec-banner {{
            color: var(--rr-gold);
        }}

        .player-card-name {{
            font-size: 1.25rem;
            font-weight: 900;
            color: #FFF;
            line-height: 1.2;
            letter-spacing: -0.3px;
        }}

        .tier-and-status {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-top: 0.3rem;
        }}

        .tier-tag {{
            font-size: 0.72rem;
            font-weight: 700;
            text-transform: uppercase;
            padding: 0.2rem 0.6rem;
            border-radius: 6px;
            letter-spacing: 0.4px;
        }}

        .tier-confirmed {{
            background: rgba(16, 185, 129, 0.15);
            color: #34D399;
            border: 1px solid rgba(16, 185, 129, 0.4);
        }}

        .tier-probable {{
            background: rgba(245, 158, 11, 0.15);
            color: #FBBF24;
            border: 1px solid rgba(245, 158, 11, 0.4);
        }}

        .tier-tossup {{
            background: rgba(239, 68, 68, 0.15);
            color: #F87171;
            border: 1px solid rgba(239, 68, 68, 0.4);
        }}

        .metrics-card-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 0.6rem;
            background: rgba(0, 0, 0, 0.3);
            border-radius: 10px;
            padding: 0.75rem 0.9rem;
            border: 1px solid rgba(255, 255, 255, 0.05);
            margin-bottom: 0.9rem;
        }}

        .metric-cell .clbl {{
            font-size: 0.68rem;
            color: var(--text-dim);
            text-transform: uppercase;
            font-weight: 700;
        }}

        .metric-cell .cval {{
            font-size: 1.15rem;
            font-weight: 800;
            color: #FFF;
            margin-top: 0.1rem;
        }}

        .metric-cell .cval.pink {{
            color: var(--rr-pink-light);
        }}

        .metric-cell .cval.gold {{
            color: #FFD700;
        }}

        .metric-cell .cval.cyan {{
            color: var(--rr-cyan);
        }}

        .match-consistency-strip {{
            font-size: 0.78rem;
            color: #CBD5E1;
            display: flex;
            justify-content: space-between;
            margin-bottom: 0.3rem;
        }}

        .bar-shell {{
            height: 6px;
            background: rgba(255, 255, 255, 0.08);
            border-radius: 3px;
            overflow: hidden;
        }}

        .bar-fill {{
            height: 100%;
            background: linear-gradient(90deg, var(--rr-pink), var(--rr-gold));
            border-radius: 3px;
        }}

        /* Table View */
        .table-container {{
            background: var(--card-bg);
            border: var(--glass-border);
            border-radius: var(--radius-lg);
            overflow: hidden;
            box-shadow: 0 4px 30px rgba(0, 0, 0, 0.25);
            margin-bottom: 2rem;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 0.88rem;
            text-align: left;
        }}

        thead th {{
            background: rgba(0, 15, 38, 0.85);
            padding: 0.9rem 1.1rem;
            font-weight: 700;
            color: #94A3B8;
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        }}

        tbody td {{
            padding: 0.85rem 1.1rem;
            border-bottom: 1px solid rgba(255, 255, 255, 0.04);
            color: #E2E8F0;
        }}

        tbody tr:hover {{
            background: rgba(255, 255, 255, 0.03);
        }}

        tbody tr.highlight-row {{
            background: rgba(228, 28, 106, 0.08);
        }}

        /* Head-to-Head Scout Comparison Tab */
        .h2h-container {{
            display: grid;
            grid-template-columns: 1fr 1.3fr 1fr;
            gap: 1.5rem;
            align-items: start;
        }}

        .scout-column {{
            background: var(--card-bg);
            border: var(--glass-border);
            border-radius: var(--radius-lg);
            padding: 1.5rem;
        }}

        .scout-column.center-radar {{
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
        }}

        .radar-canvas-container {{
            position: relative;
            width: 100%;
            max-width: 440px;
            height: 380px;
            margin: 1rem 0;
        }}

        select.player-select {{
            width: 100%;
            padding: 0.75rem 1rem;
            background: #00163A;
            border: 1px solid rgba(255, 255, 255, 0.15);
            border-radius: 10px;
            color: #FFF;
            font-size: 0.95rem;
            font-weight: 700;
            margin-bottom: 1.2rem;
            outline: none;
            cursor: pointer;
        }}

        select.player-select:focus {{
            border-color: var(--rr-pink);
            box-shadow: 0 0 10px var(--rr-pink-glow);
        }}

        .verdict-box {{
            background: rgba(228, 28, 106, 0.1);
            border: 1px solid rgba(228, 28, 106, 0.3);
            border-radius: 12px;
            padding: 1rem;
            margin-top: 1.2rem;
            font-size: 0.85rem;
            line-height: 1.5;
            color: #F8FAFC;
            text-align: left;
        }}

        /* Live Simulator Tab */
        .sim-grid {{
            display: grid;
            grid-template-columns: 1.2fr 1fr;
            gap: 1.8rem;
        }}

        .sim-controls {{
            background: var(--card-bg);
            border: var(--glass-border);
            border-radius: var(--radius-lg);
            padding: 1.8rem;
        }}

        .sim-gauge-area {{
            background: var(--card-bg);
            border: var(--glass-border);
            border-radius: var(--radius-lg);
            padding: 1.8rem;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
        }}

        .slider-group {{
            margin-bottom: 1.2rem;
        }}

        .slider-header {{
            display: flex;
            justify-content: space-between;
            font-size: 0.88rem;
            font-weight: 700;
            margin-bottom: 0.4rem;
            color: #E2E8F0;
        }}

        .slider-header span.val {{
            color: var(--rr-pink-light);
        }}

        input[type=range] {{
            width: 100%;
            height: 6px;
            border-radius: 3px;
            background: rgba(255, 255, 255, 0.12);
            outline: none;
            -webkit-appearance: none;
        }}

        input[type=range]::-webkit-slider-thumb {{
            -webkit-appearance: none;
            width: 18px;
            height: 18px;
            border-radius: 50%;
            background: var(--rr-pink);
            cursor: pointer;
            box-shadow: 0 0 10px var(--rr-pink-glow);
            border: 2px solid #FFF;
        }}

        .pressure-indicator-banner {{
            padding: 1rem 1.8rem;
            border-radius: 12px;
            font-weight: 800;
            font-size: 1.15rem;
            margin-top: 1rem;
            width: 100%;
            text-align: center;
            letter-spacing: 0.5px;
            transition: all 0.3s;
        }}

        .indicator-high {{
            background: linear-gradient(135deg, rgba(228, 28, 106, 0.3), rgba(255, 46, 126, 0.45));
            border: 2px solid var(--rr-pink);
            color: #FFF;
            box-shadow: 0 0 25px var(--rr-pink-glow);
        }}

        .indicator-ordinary {{
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.15);
            color: #94A3B8;
        }}

        /* Buttons & Actions */
        .btn-action {{
            background: linear-gradient(135deg, var(--rr-pink), #9B073D);
            border: none;
            color: #FFF;
            font-weight: 700;
            font-size: 0.88rem;
            padding: 0.6rem 1.2rem;
            border-radius: 8px;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            transition: all 0.2s;
            box-shadow: 0 4px 15px var(--rr-pink-glow);
        }}

        .btn-action:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 20px var(--rr-pink-glow);
        }}

        .btn-outline {{
            background: transparent;
            border: 1px solid rgba(255, 255, 255, 0.2);
            color: #FFF;
            font-weight: 600;
            font-size: 0.85rem;
            padding: 0.5rem 1rem;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.2s;
        }}

        .btn-outline:hover {{
            background: rgba(255, 255, 255, 0.08);
            border-color: #FFF;
        }}

        /* Player Inspection Modal */
        .modal-backdrop {{
            position: fixed;
            top: 0; left: 0; right: 0; bottom: 0;
            background: rgba(0, 0, 0, 0.75);
            backdrop-filter: blur(10px);
            z-index: 1000;
            display: none;
            align-items: center;
            justify-content: center;
            padding: 1rem;
        }}

        .modal-box {{
            background: #00163A;
            border: 1px solid rgba(228, 28, 106, 0.5);
            border-radius: 20px;
            max-width: 600px;
            width: 100%;
            padding: 2rem;
            position: relative;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.6);
            animation: modalScale 0.25s ease-out;
        }}

        @keyframes modalScale {{
            from {{ transform: scale(0.92); opacity: 0; }}
            to {{ transform: scale(1); opacity: 1; }}
        }}

        .modal-close {{
            position: absolute;
            top: 1rem; right: 1rem;
            background: transparent;
            border: none;
            color: #FFF;
            font-size: 1.5rem;
            cursor: pointer;
        }}

        /* Responsive */
        @media (max-width: 1024px) {{
            .hero-grid, .sim-grid, .h2h-container {{
                grid-template-columns: 1fr;
            }}
            .stat-cards-trio {{
                grid-template-columns: repeat(3, 1fr);
            }}
        }}

        @media (max-width: 640px) {{
            header {{
                flex-direction: column;
                gap: 0.8rem;
                padding: 0.8rem 1rem;
            }}
            .nav-tabs {{
                width: 100%;
                overflow-x: auto;
            }}
            .stat-cards-trio {{
                grid-template-columns: 1fr;
            }}
            .cards-grid-super {{
                grid-template-columns: 1fr;
            }}
        }}
    </style>
</head>
<body>

    <!-- Header Navigation -->
    <header>
        <div class="brand-area">
            <div class="rr-logo-badge">RR</div>
            <div class="brand-text">
                <h1>SupeRR SELECTOR</h1>
                <p>Rajasthan Royals · Season 2 · Round 1 Player Display</p>
            </div>
        </div>
        <div class="nav-tabs">
            <button class="nav-btn active" onclick="switchTab('leaderboard')">🏆 Cricketer Cards</button>
            <button class="nav-btn" onclick="switchTab('explorer')">🔍 Full Scout DB</button>
            <button class="nav-btn" onclick="switchTab('h2h')">⚔️ Head-to-Head</button>
            <button class="nav-btn" onclick="switchTab('simulator')">⚡ Match Sandbox</button>
            <button class="nav-btn" onclick="switchTab('audit')">📊 Audit & Proof</button>
        </div>
    </header>

    <!-- Hero Header -->
    <div class="hero-banner">
        <div class="hero-grid">
            <div class="hero-title-area">
                <h2>Who Delivers Under <span class="gradient">Real Pressure?</span></h2>
                <p class="hero-subtitle">
                    Official Top 10 Cricketer Trading Cards powered by our <strong>Leverage Index & Empirical Bayes Engine</strong>.
                    Trained across <strong>775 clean IPL & T20I matches (2022–2026)</strong> and 185,400 deliveries.
                </p>
                <div class="pill-row">
                    <span class="badge-pill pink">🎯 Top 20% Leverage = Pressure (LI ≥ 1.25)</span>
                    <span class="badge-pill gold">📈 43% All Match Swing in 20% Deliveries</span>
                    <span class="badge-pill">🛡️ Match-Clustered Bayes Shrinkage</span>
                    <span class="badge-pill">🔒 Nested Out-of-Sample Validated</span>
                </div>
            </div>
            <div class="stat-cards-trio">
                <div class="stat-card-mini">
                    <div class="val" id="stat-matches">775</div>
                    <div class="lbl">Clean Matches</div>
                </div>
                <div class="stat-card-mini">
                    <div class="val" id="stat-balls">185.4K</div>
                    <div class="lbl">Balls Analyzed</div>
                </div>
                <div class="stat-card-mini">
                    <div class="val" id="stat-swing">2.97x</div>
                    <div class="lbl">Pressure Swing</div>
                </div>
            </div>
        </div>
    </div>

    <!-- Main Content Area -->
    <main>

        <!-- TAB 1: OFFICIAL TOP 10 CRICKETER CARDS -->
        <section id="tab-leaderboard" class="tab-section active">
            <div class="section-header">
                <div class="section-title">
                    <h3>Official Top 10 Cricketer Face Cards</h3>
                    <p>Click any player card to inspect their situational breakdown and out-of-sample stability.</p>
                </div>
                <div style="display: flex; gap: 0.8rem; align-items: center;">
                    <div class="role-switcher">
                        <button class="role-btn active" id="btn-role-bat" onclick="toggleRole('bat')">Batters</button>
                        <button class="role-btn" id="btn-role-bowl" onclick="toggleRole('bowl')">Bowlers</button>
                    </div>
                    <button class="btn-action" onclick="copyUnstopList()">📋 Copy Unstop Order</button>
                </div>
            </div>

            <!-- Cricketer Ultimate Cards Grid -->
            <div class="cards-grid-super" id="cards-container">
                <!-- Injected via JS -->
            </div>

            <!-- Full Ranked Table -->
            <div class="section-header" style="margin-top: 2.5rem;">
                <div class="section-title">
                    <h3 style="font-size: 1.25rem;">Official Top 10 Submissions for Unstop Dropdown</h3>
                    <p>Exact numbers in <em>runs per 100 balls above situation expectation</em>.</p>
                </div>
            </div>
            <div class="table-container">
                <table>
                    <thead>
                        <tr>
                            <th>Rank</th>
                            <th>Player Name</th>
                            <th>Team</th>
                            <th>Stability Tier</th>
                            <th>Pressure Balls</th>
                            <th>Matches</th>
                            <th>Baseline (g)</th>
                            <th>Pressure Delta (δ)</th>
                            <th>Level (g+δ)</th>
                            <th>Hit-Rate %</th>
                            <th>Clutch Score</th>
                        </tr>
                    </thead>
                    <tbody id="top10-table-body">
                        <!-- Injected via JS -->
                    </tbody>
                </table>
            </div>

            <div style="margin-top:1.5rem;padding:1.15rem;background:rgba(255,255,255,.055);border:1px solid rgba(255,255,255,.12);border-radius:14px;">
                <h3 style="font-size:1.05rem;margin-bottom:.35rem;">Rajasthan Royals retained players</h3>
                <p style="font-size:.82rem;color:#94A3B8;margin-bottom:.9rem;">The 17 retained players you specified. Riyan Parag is captain. Each player has a portrait; if an image host is unavailable, the card shows a clean initials avatar.</p>
                <div id="rr-retained-grid" style="display:grid;grid-template-columns:repeat(auto-fill,minmax(145px,1fr));gap:.75rem;"></div>
                <div style="margin-top:1rem;padding-top:.8rem;border-top:1px solid rgba(255,255,255,.1);font-size:.78rem;color:#CBD5E1;">
                    <strong style="color:#FCA5A5">Released:</strong> <span id="rr-released-list"></span>
                    <span style="margin:0 .45rem;color:#64748B">•</span>
                    <strong style="color:#FCD34D">Trades:</strong> <span id="rr-moved-list"></span>
                </div>
            </div>
        </section>

        <!-- TAB 2: FULL PLAYER SCOUT DATABASE -->
        <section id="tab-explorer" class="tab-section">
            <div class="section-header">
                <div class="section-title">
                    <h3>Complete Player Database (91 Batters · 98 Bowlers)</h3>
                    <p>Filter, search, and explore every player meeting minimum exposure criteria.</p>
                </div>
                <div style="display: flex; gap: 0.6rem;">
                    <input type="text" id="player-search-input" placeholder="Search player name..." 
                           style="background: #00163A; border: 1px solid rgba(255,255,255,0.15); border-radius: 8px; padding: 0.5rem 0.9rem; color: #FFF; outline: none;"
                           oninput="filterExplorerTable()">
                    <select id="explorer-role-filter" class="btn-outline" onchange="filterExplorerTable()">
                        <option value="bat">Batters</option>
                        <option value="bowl">Bowlers</option>
                    </select>
                    <select id="explorer-tier-filter" class="btn-outline" onchange="filterExplorerTable()">
                        <option value="all">All Tiers</option>
                        <option value="Confirmed">Confirmed</option>
                        <option value="Probable">Probable</option>
                        <option value="Toss-up">Toss-up</option>
                    </select>
                </div>
            </div>

            <div class="table-container">
                <table>
                    <thead>
                        <tr>
                            <th>Rank</th>
                            <th>Player</th>
                            <th>Team</th>
                            <th>Tier</th>
                            <th>Pressure Balls</th>
                            <th>Ordinary Balls</th>
                            <th>Matches</th>
                            <th>Baseline g</th>
                            <th>Delta δ</th>
                            <th>Level under Pressure</th>
                            <th>Hit-Rate</th>
                            <th>Clutch Score</th>
                            <th>Action</th>
                        </tr>
                    </thead>
                    <tbody id="explorer-table-body">
                        <!-- Injected via JS -->
                    </tbody>
                </table>
            </div>
        </section>

        <!-- TAB 3: HEAD-TO-HEAD SCOUT COMPARISON -->
        <section id="tab-h2h" class="tab-section">
            <div class="section-header">
                <div class="section-title">
                    <h3>Head-to-Head Scout Comparison</h3>
                    <p>Select any two players to compare face profiles, radar metrics, and statistical dominance.</p>
                </div>
                <div class="role-switcher">
                    <button class="role-btn active" id="h2h-bat-btn" onclick="setH2HRole('bat')">Batters</button>
                    <button class="role-btn" id="h2h-bowl-btn" onclick="setH2HRole('bowl')">Bowlers</button>
                </div>
            </div>

            <div class="h2h-container">
                <!-- Player A -->
                <div class="scout-column">
                    <label style="font-size: 0.75rem; text-transform: uppercase; font-weight: 700; color: var(--rr-pink);">Player A</label>
                    <select id="player-select-a" class="player-select" onchange="updateH2HComparison()"></select>
                    <div id="player-a-stats"></div>
                </div>

                <!-- Center Radar Chart -->
                <div class="scout-column center-radar">
                    <h4 style="font-weight: 800; font-size: 1.1rem; color: #FFF;">Multidimensional Pressure Radar</h4>
                    <p style="font-size: 0.78rem; color: var(--text-muted); margin-bottom: 0.5rem;">Normalized 0–100 Percentile Scale</p>
                    <div class="radar-canvas-container">
                        <canvas id="radarChart" width="420" height="360"></canvas>
                    </div>
                    <div id="h2h-verdict" class="verdict-box">
                        <!-- AI Scout commentary injected here -->
                    </div>
                </div>

                <!-- Player B -->
                <div class="scout-column">
                    <label style="font-size: 0.75rem; text-transform: uppercase; font-weight: 700; color: var(--rr-cyan);">Player B</label>
                    <select id="player-select-b" class="player-select" onchange="updateH2HComparison()"></select>
                    <div id="player-b-stats"></div>
                </div>
            </div>
        </section>

        <!-- TAB 4: LIVE WIN-PROBABILITY & LEVERAGE SANDBOX -->
        <section id="tab-simulator" class="tab-section">
            <div class="section-header">
                <div class="section-title">
                    <h3>Match State Leverage & Win-Probability Simulator</h3>
                    <p>Interactive implementation of the out-of-fold logistic win-probability model and leverage index formula.</p>
                </div>
                <button class="btn-outline" onclick="resetSimDefaults()">↺ Reset to Death Chase</button>
            </div>

            <div class="sim-grid">
                <!-- Controls -->
                <div class="sim-controls">
                    <div class="slider-group">
                        <div class="slider-header">
                            <span>Innings</span>
                            <span class="val" id="sim-inn-val">2nd (Chase)</span>
                        </div>
                        <div style="display: flex; gap: 0.5rem; margin-top: 0.4rem;">
                            <button class="btn-outline" id="sim-inn1-btn" onclick="setSimInnings(1)" style="flex:1;">1st Innings (Setting)</button>
                            <button class="btn-outline" id="sim-inn2-btn" onclick="setSimInnings(2)" style="flex:1; border-color: var(--rr-pink); background: rgba(228,28,106,0.15);">2nd Innings (Chasing)</button>
                        </div>
                    </div>

                    <div class="slider-group">
                        <div class="slider-header">
                            <span>Balls Remaining</span>
                            <span class="val" id="sim-balls-val">12 balls (2.0 overs)</span>
                        </div>
                        <input type="range" id="sim-balls" min="1" max="120" value="12" oninput="runSimCalc()">
                    </div>

                    <div class="slider-group">
                        <div class="slider-header">
                            <span>Wickets Lost</span>
                            <span class="val" id="sim-wk-val">5 wickets</span>
                        </div>
                        <input type="range" id="sim-wk" min="0" max="9" value="5" oninput="runSimCalc()">
                    </div>

                    <div class="slider-group" id="sim-need-group">
                        <div class="slider-header">
                            <span>Runs Needed to Win</span>
                            <span class="val" id="sim-need-val">28 runs</span>
                        </div>
                        <input type="range" id="sim-need" min="1" max="120" value="28" oninput="runSimCalc()">
                    </div>

                    <div class="slider-group">
                        <div class="slider-header">
                            <span>Venue Par Score (Historical Ground Average)</span>
                            <span class="val" id="sim-par-val">175</span>
                        </div>
                        <input type="range" id="sim-par" min="130" max="230" value="175" oninput="runSimCalc()">
                    </div>

                    <div class="slider-group">
                        <div class="slider-header">
                            <span>Team Elo Difference (Batting − Bowling)</span>
                            <span class="val" id="sim-elo-val">+0 (Even Match)</span>
                        </div>
                        <input type="range" id="sim-elo" min="-200" max="200" value="0" oninput="runSimCalc()">
                    </div>
                </div>

                <!-- Live Results Gauge -->
                <div class="sim-gauge-area">
                    <h4 style="font-weight: 700; color: var(--text-muted); font-size: 0.85rem; text-transform: uppercase;">Current Win Probability (Batting Team)</h4>
                    <div style="font-size: 3.5rem; font-weight: 900; margin: 0.5rem 0;" id="sim-wp-display">48.2%</div>
                    
                    <div style="width: 100%; height: 8px; background: rgba(255,255,255,0.1); border-radius: 4px; overflow: hidden; margin-bottom: 1.5rem;">
                        <div id="sim-wp-bar" style="height: 100%; width: 48.2%; background: linear-gradient(90deg, #FF2E7E, #FFD700); border-radius: 4px;"></div>
                    </div>

                    <h4 style="font-weight: 700; color: var(--text-muted); font-size: 0.85rem; text-transform: uppercase;">Leverage Index (LI)</h4>
                    <div style="font-size: 2.8rem; font-weight: 800; color: var(--rr-pink-light); margin: 0.3rem 0;" id="sim-li-display">2.84</div>
                    <p style="font-size: 0.82rem; color: var(--text-muted);">1.0 = Average Ball in T20 Cricket</p>

                    <div id="sim-pressure-banner" class="pressure-indicator-banner indicator-high">
                        🔥 HIGH PRESSURE BALL (Top 20% Threshold: LI ≥ 1.25)
                    </div>

                    <div style="margin-top: 1.5rem; width: 100%; text-align: left; background: rgba(0,0,0,0.25); padding: 1rem; border-radius: 10px; font-size: 0.82rem;">
                        <div style="font-weight: 700; margin-bottom: 0.5rem; color: #FFD700;">Counterfactual Win-Prob Swing on Next Delivery:</div>
                        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 0.5rem; text-align: center;" id="sim-counterfactuals">
                            <!-- Injected by JS -->
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- TAB 5: AUDIT & RIGOR -->
        <section id="tab-audit" class="tab-section">
            <div class="section-header">
                <div class="section-title">
                    <h3>Empirical Audit & Scientific Verification</h3>
                    <p>Evidence that our leverage-based method beats heuristic rules and survives strict nested cross-validation.</p>
                </div>
            </div>

            <!-- Experiment B Table -->
            <div class="table-container">
                <div style="padding: 1.2rem; background: rgba(0, 15, 38, 0.8); border-bottom: 1px solid rgba(255,255,255,0.08);">
                    <h4 style="font-size: 1.1rem; font-weight: 800; color: #FFF;">Matched Head-to-Head Out-of-Sample Performance (Experiment B)</h4>
                    <p style="font-size: 0.82rem; color: var(--text-muted); margin-top: 0.2rem;">Evaluated on strictly identical held-out players and matches across 12 random splits (Spearman Rank Correlation ρ).</p>
                </div>
                <table>
                    <thead>
                        <tr>
                            <th>Evaluation Scope</th>
                            <th>Target Metric</th>
                            <th>Our Model (Leverage)</th>
                            <th>Percentile Composite (Rule)</th>
                            <th>Usual Level Only</th>
                            <th>Verdict</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><strong>Batters (Not Nested)</strong></td>
                            <td>Pressure Value (Our Flag)</td>
                            <td style="color:#FFD700; font-weight:800;">0.273</td>
                            <td>0.156</td>
                            <td>0.264</td>
                            <td><span class="badge-pill pink">+75% over Rule Composite</span></td>
                        </tr>
                        <tr>
                            <td><strong>Batters (Fully Nested)</strong></td>
                            <td>Pressure Value (Our Flag)</td>
                            <td style="color:#FFD700; font-weight:800;">0.119</td>
                            <td>0.052</td>
                            <td>0.160</td>
                            <td><span class="badge-pill pink">More than double composite</span></td>
                        </tr>
                        <tr>
                            <td><strong>Batters (Fully Nested)</strong></td>
                            <td>Rule-Flag Strike Rate</td>
                            <td>0.160</td>
                            <td>0.103</td>
                            <td style="color:#FFD700; font-weight:800;">0.274</td>
                            <td><span class="badge-pill">Usual level strong predictor</span></td>
                        </tr>
                        <tr>
                            <td><strong>Bowlers (Not Nested)</strong></td>
                            <td>Pressure Value (Our Flag)</td>
                            <td style="color:#FFD700; font-weight:800;">0.275</td>
                            <td>0.147</td>
                            <td>0.266</td>
                            <td><span class="badge-pill pink">+87% over Rule Composite</span></td>
                        </tr>
                        <tr>
                            <td><strong>Bowlers (Fully Nested)</strong></td>
                            <td>Pressure Value (Our Flag)</td>
                            <td style="color:#FFD700; font-weight:800;">0.207</td>
                            <td>0.141</td>
                            <td>0.171</td>
                            <td><span class="badge-pill pink">Clear leader on value</span></td>
                        </tr>
                        <tr>
                            <td><strong>Bowlers (Fully Nested)</strong></td>
                            <td>Rule-Flag −Economy</td>
                            <td style="color:#FFD700; font-weight:800;">0.302</td>
                            <td>0.274</td>
                            <td>0.298</td>
                            <td><span class="badge-pill pink">Beats both benchmarks</span></td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <!-- Case Studies Grid -->
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin-top: 1.5rem;">
                <div class="scout-column">
                    <h4 style="color: #FFD700; font-size: 1.1rem; margin-bottom: 0.6rem;">Case 1: The Virat Kohli Anchor Paradox</h4>
                    <p style="font-size: 0.86rem; color: #CBD5E1; line-height: 1.6;">
                        <strong>Rank 84 of 91 eligible batters.</strong> Why? Kohli is clearly above average on high-pressure balls (+12 runs per 100 balls) and positive in 19 of 27 pressure matches. However, our situation-matched metric evaluates <em>per-ball run efficiency above situation expectation</em>. Anchoring through the middle overs with lower strike-rate lowers his baseline <em>g</em> (−1.1). Our report honestly highlights this as an inherent model property: per-ball value favors aggressive power-hitters over batting-through anchors.
                    </p>
                </div>
                <div class="scout-column">
                    <h4 style="color: var(--rr-cyan); font-size: 1.1rem; margin-bottom: 0.6rem;">Case 2: Sunil Narine & Jasprit Bumrah</h4>
                    <p style="font-size: 0.86rem; color: #CBD5E1; line-height: 1.6;">
                        <strong>Rank 1 and Rank 3 Bowlers.</strong> Sunil Narine maintains an extraordinary baseline (<em>g</em> = 19.8) and holds it under pressure (δ = +0.73), with 17 positive matches out of 23. In contrast, Jasprit Bumrah has a negative pressure jump (δ = −6.0) because teams take minimal risk against him under pressure, yet his baseline is so phenomenal (<em>g</em> = 20.4) that he still finishes 3rd overall. High ranking reflects <em>who delivers</em>, not a mythical clutch gene.
                    </p>
                </div>
            </div>
        </section>

    </main>

    <!-- Player Inspection Modal -->
    <div id="player-modal" class="modal-backdrop" onclick="closeModal(event)">
        <div class="modal-box" onclick="event.stopPropagation()">
            <button class="modal-close" onclick="closeModal()">×</button>
            <div id="modal-content"></div>
        </div>
    </div>

    <!-- Embedded Data Object -->
    <script>
        const APP_DATA = {data_json_str};
        let currentRole = "bat";
        let currentH2HRole = "bat";
        let simInnings = 2;

        // Initialize App
        document.addEventListener("DOMContentLoaded", () => {{
            renderLeaderboard();
            populateExplorer();
            renderRRSquad();
            initH2H();
            runSimCalc();
        }});

        function switchTab(tabId) {{
            document.querySelectorAll(".tab-section").forEach(el => el.classList.remove("active"));
            document.querySelectorAll(".nav-btn").forEach(el => el.classList.remove("active"));
            
            document.getElementById("tab-" + tabId).classList.add("active");
            const btns = document.querySelectorAll(".nav-btn");
            const tabOrder = ["leaderboard", "explorer", "h2h", "simulator", "audit"];
            const idx = tabOrder.indexOf(tabId);
            if (idx >= 0 && btns[idx]) btns[idx].classList.add("active");

            if (tabId === "h2h") {{
                setTimeout(drawRadar, 50);
            }}
        }}

        function toggleRole(role) {{
            currentRole = role;
            document.getElementById("btn-role-bat").classList.toggle("active", role === "bat");
            document.getElementById("btn-role-bowl").classList.toggle("active", role === "bowl");
            renderLeaderboard();
        }}

        function renderRRSquad() {{
            const grid = document.getElementById("rr-retained-grid");
            if (!grid) return;
            const players = APP_DATA.rr_retained_players || [];
            grid.innerHTML = players.map((p, i) => `
                <article style="min-width:0;padding:.75rem;background:rgba(0,15,38,.55);border:1px solid rgba(255,255,255,.09);border-radius:12px;text-align:center">
                    <img src="${{p.img}}" alt="${{p.name}}" loading="lazy" style="width:100%;height:126px;object-fit:contain;object-position:center bottom;border-radius:8px;background:radial-gradient(circle at 50% 35%,rgba(228,28,106,.22),transparent 70%)" onerror="this.onerror=null;this.src=getSvgAvatar('${{p.name}}','RR','')">
                    <div style="font-weight:800;font-size:.85rem;margin-top:.55rem">${{p.name}}</div>
                    <div style="font-size:.67rem;color:#94A3B8;margin-top:.2rem">${{p.captain ? 'CAPTAIN · RETAINED' : 'RETAINED'}}</div>
                </article>`).join("");
            document.getElementById("rr-released-list").textContent = (APP_DATA.rr_released_players || []).join(", ") || "None listed";
            document.getElementById("rr-moved-list").textContent = (APP_DATA.rr_moved_players || []).map(p => `${{p.name}} — ${{p.status}}`).join(", ") || "None listed";
        }}

        // Generate SVG Avatar fallback
        function getSvgAvatar(name, team, jersey) {{
            const initials = name.split(" ").map(n => n[0]).join("").slice(0, 2);
            const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="200" height="200" viewBox="0 0 200 200"><defs><linearGradient id="g" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#E41C6A"/><stop offset="100%" stop-color="#07224F"/></linearGradient></defs><rect width="200" height="200" rx="20" fill="url(#g)"/><circle cx="100" cy="80" r="45" fill="#FFFFFF" opacity="0.15"/><text x="100" y="95" font-family="sans-serif" font-weight="900" font-size="44" fill="#FFFFFF" text-anchor="middle">${{initials}}</text><rect x="40" y="145" width="120" height="30" rx="8" fill="#000000" opacity="0.4"/><text x="100" y="165" font-family="sans-serif" font-weight="800" font-size="14" fill="#FFD700" text-anchor="middle">${{team}} #${{jersey}}</text></svg>`;
            return "data:image/svg+xml;charset=UTF-8," + encodeURIComponent(svg);
        }}

        function renderLeaderboard() {{
            const list = currentRole === "bat" ? APP_DATA.top10_batters : APP_DATA.top10_bowlers;
            const container = document.getElementById("cards-container");
            const tableBody = document.getElementById("top10-table-body");
            
            container.innerHTML = "";
            tableBody.innerHTML = "";

            list.forEach(p => {{
                const tierClass = p.tier === "Confirmed" ? "tier-confirmed" : (p.tier === "Probable" ? "tier-probable" : "tier-tossup");
                const rankClass = "rank-" + p.rank;
                const scoreFmt = p.score.toFixed(2);
                const levelFmt = (p.level >= 0 ? "+" : "") + p.level.toFixed(2);
                const hitRatePct = Math.round((p.hit / p.hit_n) * 100);
                const fallbackSvg = getSvgAvatar(p.name, p.team || "T20", p.jersey || "00");

                // Cricketer Face Card
                const card = document.createElement("div");
                card.className = `cricketer-card ${{rankClass}}`;
                card.onclick = () => openPlayerModal(p.name, currentRole);
                card.innerHTML = `
                    <div class="card-stage">
                        <div class="card-overlay-badge-left">
                            <span class="ovr-box">${{p.rating || 90}}</span>
                            <span class="ovr-lbl">CLU OVR</span>
                            <span class="team-pill">${{p.team || "T20"}} #${{p.jersey || "0"}}</span>
                            <span class="country-flag">${{p.flag || "🏏"}}</span>
                        </div>
                        <div class="card-overlay-badge-right">
                            <span class="rank-tag-large">#${{p.rank}}</span>
                            <span class="tier-tag ${{tierClass}}">${{p.tier}}</span>
                        </div>
                        <img class="player-headshot-img" 
                             src="${{p.img}}" 
                             alt="${{p.name}}"
                             onerror="if(this.src!=='${{p.backup_img}}'){{this.src='${{p.backup_img}}';}}else{{this.src='${{fallbackSvg}}';}}">
                    </div>
                    <div class="card-content">
                        <div class="player-name-title-row">
                            <div class="player-spec-banner">${{p.title || "CLUTCH PERFORMER"}}</div>
                            <div class="player-card-name">${{p.name}}</div>
                        </div>
                        <div class="metrics-card-grid">
                            <div class="metric-cell">
                                <div class="clbl">Clutch Index</div>
                                <div class="cval pink">${{scoreFmt}}</div>
                            </div>
                            <div class="metric-cell">
                                <div class="clbl">Pressure Level</div>
                                <div class="cval gold">${{levelFmt}}</div>
                            </div>
                            <div class="metric-cell">
                                <div class="clbl">Baseline Skill (g)</div>
                                <div class="cval">${{p.g ? p.g.toFixed(1) : "0.0"}}</div>
                            </div>
                            <div class="metric-cell">
                                <div class="clbl">Pressure Delta (δ)</div>
                                <div class="cval cyan">${{(p.delta >= 0 ? "+" : "") + (p.delta ? p.delta.toFixed(1) : "0.0")}}</div>
                            </div>
                        </div>
                        <div>
                            <div class="match-consistency-strip">
                                <span>Clutch Consistency</span>
                                <span style="font-weight: 700; color: #FFF;">${{p.hit}} / ${{p.hit_n}} (${{hitRatePct}}%)</span>
                            </div>
                            <div class="bar-shell"><div class="bar-fill" style="width: ${{hitRatePct}}%;"></div></div>
                        </div>
                    </div>
                `;
                container.appendChild(card);

                // Table Row
                const row = document.createElement("tr");
                if (p.rank <= 3) row.className = "highlight-row";
                row.innerHTML = `
                    <td style="font-weight: 900; font-size: 1.05rem;">#${{p.rank}}</td>
                    <td style="font-weight: 700; color: #FFF;">
                        <span style="margin-right: 0.35rem;">${{p.flag || ""}}</span>${{p.name}}
                    </td>
                    <td><span class="team-pill">${{p.team || "T20"}}</span></td>
                    <td><span class="tier-tag ${{tierClass}}">${{p.tier}}</span></td>
                    <td>${{p.pb}}</td>
                    <td>${{p.pm}}</td>
                    <td>${{(p.g || 0).toFixed(1)}}</td>
                    <td>${{((p.delta || 0) >= 0 ? "+" : "") + (p.delta || 0).toFixed(1)}}</td>
                    <td style="font-weight: 700;">${{levelFmt}}</td>
                    <td>${{p.hit}}/${{p.hit_n}} (${{hitRatePct}}%)</td>
                    <td style="font-weight: 900; color: var(--rr-pink-light);">${{scoreFmt}}</td>
                `;
                tableBody.appendChild(row);
            }});
        }}

        function copyUnstopList() {{
            const list = currentRole === "bat" ? APP_DATA.top10_batters : APP_DATA.top10_bowlers;
            const text = list.map(p => `${{p.rank}}. ${{p.name}}`).join("\\n");
            navigator.clipboard.writeText(text).then(() => {{
                alert(`Top 10 ${{currentRole === "bat" ? "Batters" : "Bowlers"}} copied to clipboard in official Unstop order!`);
            }});
        }}

        /* Modal Inspector */
        function openPlayerModal(name, role) {{
            const list = role === "bat" ? APP_DATA.all_batters : APP_DATA.all_bowlers;
            const p = list.find(x => x.name === name) || list[0];
            const modal = document.getElementById("player-modal");
            const content = document.getElementById("modal-content");
            const fallbackSvg = getSvgAvatar(p.name, p.team || "T20", p.jersey || "00");

            content.innerHTML = `
                <div style="display: flex; gap: 1.5rem; align-items: center; margin-bottom: 1.5rem;">
                    <img src="${{p.img}}" 
                         alt="${{p.name}}"
                         onerror="this.src='${{fallbackSvg}}';"
                         style="width: 110px; height: 110px; border-radius: 16px; object-fit: contain; background: rgba(0,0,0,0.3); border: 2px solid var(--rr-pink);">
                    <div>
                        <div style="font-size: 0.75rem; font-weight: 800; color: var(--rr-gold); letter-spacing: 0.5px;">${{p.title || "PLAYER PROFILE"}}</div>
                        <h3 style="font-size: 1.6rem; font-weight: 900; color: #FFF; margin: 0.2rem 0;">${{p.name}}</h3>
                        <div style="display: flex; gap: 0.5rem; font-size: 0.8rem; color: var(--text-muted);">
                            <span>${{p.flag || ""}} ${{p.country || ""}}</span>
                            <span>•</span>
                            <span>${{p.team || "T20"}} #${{p.jersey || "0"}}</span>
                            <span>•</span>
                            <span style="color: var(--rr-pink-light); font-weight: 700;">Rank #${{p.rank}} (${{p.tier}})</span>
                        </div>
                    </div>
                </div>
                <div class="metrics-card-grid" style="grid-template-columns: repeat(3, 1fr); margin-bottom: 1.2rem;">
                    <div class="metric-cell">
                        <div class="clbl">Clutch Index</div>
                        <div class="cval pink">${{p.score.toFixed(2)}}</div>
                    </div>
                    <div class="metric-cell">
                        <div class="clbl">Pressure Level</div>
                        <div class="cval gold">+${{p.level.toFixed(2)}}</div>
                    </div>
                    <div class="metric-cell">
                        <div class="clbl">Baseline Skill (g)</div>
                        <div class="cval">${{p.g.toFixed(1)}}</div>
                    </div>
                    <div class="metric-cell">
                        <div class="clbl">Pressure Delta (δ)</div>
                        <div class="cval cyan">${{(p.delta >= 0 ? "+" : "") + p.delta.toFixed(1)}}</div>
                    </div>
                    <div class="metric-cell">
                        <div class="clbl">Pressure Balls</div>
                        <div class="cval">${{p.pb}}</div>
                    </div>
                    <div class="metric-cell">
                        <div class="clbl">Matches Positive</div>
                        <div class="cval">${{p.hit}} / ${{p.hit_n}}</div>
                    </div>
                </div>
                <div style="background: rgba(0,0,0,0.3); border-radius: 10px; padding: 1rem; font-size: 0.85rem; line-height: 1.5; color: #E2E8F0; margin-bottom: 1.2rem;">
                    <strong>Situational Splits:</strong><br>
                    • Chasing (Innings 2): <strong>${{p.chase_level !== null ? "+" + p.chase_level : "N/A"}}</strong> runs/100<br>
                    • Knockout Playoff Games: <strong>${{p.ko_diff !== null ? (p.ko_diff >= 0 ? "+" : "") + p.ko_diff : "N/A"}}</strong> diff vs regular<br>
                    • Long-Shot Encounters (Win Prob &lt; 25%): <strong>${{p.longshot_level !== null ? "+" + p.longshot_level : "N/A"}}</strong> runs/100
                </div>
                <button class="btn-action" style="width: 100%; justify-content: center;" onclick="inspectInH2H('${{p.name}}', '${{role}}'); closeModal();">
                    Open in Head-to-Head Scout Radar ⚔️
                </button>
            `;
            modal.style.display = "flex";
        }}

        function closeModal(e) {{
            document.getElementById("player-modal").style.display = "none";
        }}

        /* Explorer Tab */
        function populateExplorer() {{
            filterExplorerTable();
        }}

        function filterExplorerTable() {{
            const role = document.getElementById("explorer-role-filter").value;
            const tier = document.getElementById("explorer-tier-filter").value;
            const search = document.getElementById("player-search-input").value.toLowerCase();
            const list = role === "bat" ? APP_DATA.all_batters : APP_DATA.all_bowlers;
            const tbody = document.getElementById("explorer-table-body");
            tbody.innerHTML = "";

            const filtered = list.filter(p => {{
                const matchSearch = p.name.toLowerCase().includes(search);
                const matchTier = tier === "all" || p.tier === tier;
                return matchSearch && matchTier;
            }});

            filtered.forEach(p => {{
                const tierClass = p.tier === "Confirmed" ? "tier-confirmed" : (p.tier === "Probable" ? "tier-probable" : "tier-tossup");
                const row = document.createElement("tr");
                row.innerHTML = `
                    <td style="font-weight: 700;">#${{p.rank}}</td>
                    <td style="font-weight: 700; color: #FFF;">
                        <span style="margin-right: 0.35rem;">${{p.flag || ""}}</span>${{p.name}}
                    </td>
                    <td><span class="team-pill">${{p.team || "T20"}}</span></td>
                    <td><span class="tier-tag ${{tierClass}}">${{p.tier}}</span></td>
                    <td>${{p.pb}}</td>
                    <td>${{p.ob}}</td>
                    <td>${{p.pm}}</td>
                    <td>${{p.g.toFixed(1)}}</td>
                    <td>${{(p.delta >= 0 ? "+" : "") + p.delta.toFixed(1)}}</td>
                    <td style="font-weight: 700;">${{p.level.toFixed(2)}}</td>
                    <td>${{Math.round((p.hit_eb || (p.hit/p.hit_n)) * 100)}}%</td>
                    <td style="font-weight: 800; color: var(--rr-pink-light);">${{p.score.toFixed(2)}}</td>
                    <td>
                        <button class="btn-outline" style="padding: 0.25rem 0.6rem; font-size: 0.72rem;" onclick="openPlayerModal('${{p.name}}', '${{role}}')">Face Card 🎴</button>
                    </td>
                `;
                tbody.appendChild(row);
            }});
        }}

        /* Head-to-Head Comparison */
        function setH2HRole(role) {{
            currentH2HRole = role;
            document.getElementById("h2h-bat-btn").classList.toggle("active", role === "bat");
            document.getElementById("h2h-bowl-btn").classList.toggle("active", role === "bowl");
            initH2H();
        }}

        function initH2H() {{
            const list = currentH2HRole === "bat" ? APP_DATA.all_batters : APP_DATA.all_bowlers;
            const selA = document.getElementById("player-select-a");
            const selB = document.getElementById("player-select-b");

            selA.innerHTML = "";
            selB.innerHTML = "";

            list.forEach(p => {{
                const optA = document.createElement("option");
                optA.value = p.name;
                optA.textContent = `#${{p.rank}} ${{p.name}} (${{p.tier}})`;
                selA.appendChild(optA);

                const optB = document.createElement("option");
                optB.value = p.name;
                optB.textContent = `#${{p.rank}} ${{p.name}} (${{p.tier}})`;
                selB.appendChild(optB);
            }});

            if (list.length > 1) {{
                selA.selectedIndex = 0;
                selB.selectedIndex = 1;
            }}
            updateH2HComparison();
        }}

        function inspectInH2H(playerName, role) {{
            switchTab("h2h");
            if (currentH2HRole !== role) setH2HRole(role);
            const selB = document.getElementById("player-select-b");
            selB.value = playerName;
            updateH2HComparison();
        }}

        function updateH2HComparison() {{
            const list = currentH2HRole === "bat" ? APP_DATA.all_batters : APP_DATA.all_bowlers;
            const nameA = document.getElementById("player-select-a").value;
            const nameB = document.getElementById("player-select-b").value;

            const pA = list.find(p => p.name === nameA) || list[0];
            const pB = list.find(p => p.name === nameB) || list[1];

            renderPlayerCol(pA, "player-a-stats", "var(--rr-pink)");
            renderPlayerCol(pB, "player-b-stats", "var(--rr-cyan)");

            // AI Scout Verdict
            const verdictBox = document.getElementById("h2h-verdict");
            const diffScore = (pA.score - pB.score).toFixed(2);
            const winner = pA.score >= pB.score ? pA : pB;
            const loser = pA.score >= pB.score ? pB : pA;
            verdictBox.innerHTML = `
                <div style="font-weight: 800; font-size: 0.95rem; margin-bottom: 0.3rem; color: #FFD700;">
                    Scout Verdict: ${{winner.name}} holds statistical edge (+${{Math.abs(diffScore)}} runs/100)
                </div>
                <div>
                    <strong>${{winner.name}}</strong> ranks higher primarily due to a superior 
                    ${{winner.g > loser.g ? "baseline foundation (g = " + winner.g.toFixed(1) + " vs " + loser.g.toFixed(1) + ")" : "pressure-specific spike (δ = " + winner.delta.toFixed(1) + " vs " + loser.delta.toFixed(1) + ")"}} 
                    and a match success hit-rate of ${{Math.round((winner.hit/winner.hit_n)*100)}}% across ${{winner.pm}} clutch encounters.
                </div>
            `;

            drawRadar();
        }}

        function renderPlayerCol(p, elId, accentColor) {{
            const hitRate = Math.round((p.hit / p.hit_n) * 100);
            const chaseVal = p.chase_level !== null ? `+${{p.chase_level}}` : "N/A";
            const koVal = p.ko_diff !== null ? `${{p.ko_diff >= 0 ? "+" : ""}}${{p.ko_diff}}` : "N/A";
            const lsVal = p.longshot_level !== null ? `+${{p.longshot_level}}` : "N/A";
            const fallbackSvg = getSvgAvatar(p.name, p.team || "T20", p.jersey || "00");

            document.getElementById(elId).innerHTML = `
                <div style="background: rgba(0,0,0,0.3); border-radius: 14px; padding: 1.2rem; border-top: 3px solid ${{accentColor}};">
                    <div style="display: flex; gap: 1rem; align-items: center; margin-bottom: 1rem;">
                        <img src="${{p.img}}" 
                             alt="${{p.name}}"
                             onerror="this.src='${{fallbackSvg}}';"
                             style="width: 70px; height: 70px; border-radius: 12px; object-fit: contain; background: rgba(0,0,0,0.4); border: 1px solid ${{accentColor}};">
                        <div>
                            <div style="font-size: 1.4rem; font-weight: 900; color: #FFF;">${{p.score.toFixed(2)}}</div>
                            <div style="font-size: 0.8rem; font-weight: 700; color: ${{accentColor}};">Rank #${{p.rank}} (${{p.tier}})</div>
                            <div style="font-size: 0.72rem; color: var(--text-muted);">${{p.team || "T20"}} #${{p.jersey || "0"}}</div>
                        </div>
                    </div>
                    <div class="metric-bars" style="gap: 0.65rem; font-size: 0.82rem;">
                        <div class="metric-row"><span>Predicted Pressure Level:</span><span class="val">+${{p.level.toFixed(2)}}</span></div>
                        <div class="metric-row"><span>Baseline Skill (g):</span><span class="val">${{p.g.toFixed(2)}}</span></div>
                        <div class="metric-row"><span>Pressure Delta (δ):</span><span class="val">${{(p.delta>=0?"+":"")+p.delta.toFixed(2)}}</span></div>
                        <div class="metric-row"><span>Clutch Hit-Rate:</span><span class="val">${{p.hit}}/${{p.hit_n}} (${{hitRate}}%)</span></div>
                        <div class="metric-row"><span>Pressure Balls Faced:</span><span class="val">${{p.pb}} balls</span></div>
                        <div class="metric-row"><span>Chasing Value (Inn 2):</span><span class="val">${{chaseVal}}</span></div>
                        <div class="metric-row"><span>Knockout Difference:</span><span class="val">${{koVal}}</span></div>
                        <div class="metric-row"><span>Long-Shot Chases (&lt;25%):</span><span class="val">${{lsVal}}</span></div>
                    </div>
                </div>
            `;
        }}

        function drawRadar() {{
            const canvas = document.getElementById("radarChart");
            if (!canvas) return;
            const ctx = canvas.getContext("2d");
            const w = canvas.width;
            const h = canvas.height;
            const cx = w / 2;
            const cy = h / 2;
            const r = 120;

            ctx.clearRect(0, 0, w, h);

            const list = currentH2HRole === "bat" ? APP_DATA.all_batters : APP_DATA.all_bowlers;
            const nameA = document.getElementById("player-select-a").value;
            const nameB = document.getElementById("player-select-b").value;
            const pA = list.find(p => p.name === nameA) || list[0];
            const pB = list.find(p => p.name === nameB) || list[1];

            const categories = [
                "Baseline Level",
                "Pressure Delta",
                "Hit Rate %",
                "Volume (Balls)",
                "Chase Impact",
                "Knockout Boost"
            ];
            const numSides = categories.length;

            // Draw circular grid webs
            ctx.strokeStyle = "rgba(255, 255, 255, 0.1)";
            ctx.lineWidth = 1;
            for (let level = 1; level <= 4; level++) {{
                const curR = (r / 4) * level;
                ctx.beginPath();
                for (let i = 0; i < numSides; i++) {{
                    const angle = (i * 2 * Math.PI) / numSides - Math.PI / 2;
                    const x = cx + curR * Math.cos(angle);
                    const y = cy + curR * Math.sin(angle);
                    if (i === 0) ctx.moveTo(x, y);
                    else ctx.lineTo(x, y);
                }}
                ctx.closePath();
                ctx.stroke();
            }}

            // Draw axis spokes and labels
            ctx.fillStyle = "#94A3B8";
            ctx.font = "11px Outfit, sans-serif";
            ctx.textAlign = "center";
            ctx.textBaseline = "middle";

            for (let i = 0; i < numSides; i++) {{
                const angle = (i * 2 * Math.PI) / numSides - Math.PI / 2;
                const x = cx + r * Math.cos(angle);
                const y = cy + r * Math.sin(angle);
                ctx.beginPath();
                ctx.moveTo(cx, cy);
                ctx.lineTo(x, y);
                ctx.stroke();

                const lx = cx + (r + 26) * Math.cos(angle);
                const ly = cy + (r + 20) * Math.sin(angle);
                ctx.fillText(categories[i], lx, ly);
            }}

            // Normalization helper
            function getNormValues(p) {{
                const hit = p.hit / p.hit_n;
                const v1 = Math.min(Math.max((p.g + 10) / 40, 0.1), 1.0);
                const v2 = Math.min(Math.max((p.delta + 10) / 30, 0.1), 1.0);
                const v3 = Math.min(Math.max(hit, 0.2), 1.0);
                const v4 = Math.min(Math.max(p.pb / 550, 0.15), 1.0);
                const v5 = Math.min(Math.max(((p.chase_level || p.level) + 5) / 35, 0.1), 1.0);
                const v6 = Math.min(Math.max(((p.ko_diff || 0) + 20) / 60, 0.1), 1.0);
                return [v1, v2, v3, v4, v5, v6];
            }}

            function drawPlayerPolygon(vals, color, fillColor) {{
                ctx.beginPath();
                for (let i = 0; i < numSides; i++) {{
                    const angle = (i * 2 * Math.PI) / numSides - Math.PI / 2;
                    const valR = r * vals[i];
                    const x = cx + valR * Math.cos(angle);
                    const y = cy + valR * Math.sin(angle);
                    if (i === 0) ctx.moveTo(x, y);
                    else ctx.lineTo(x, y);
                }}
                ctx.closePath();
                ctx.fillStyle = fillColor;
                ctx.fill();
                ctx.strokeStyle = color;
                ctx.lineWidth = 2.5;
                ctx.stroke();
            }}

            drawPlayerPolygon(getNormValues(pA), "#E41C6A", "rgba(228, 28, 106, 0.25)");
            drawPlayerPolygon(getNormValues(pB), "#00E5FF", "rgba(0, 229, 255, 0.2)");
        }}

        /* Tab 4: Match State Simulator */
        function setSimInnings(inn) {{
            simInnings = inn;
            document.getElementById("sim-inn1-btn").style.borderColor = inn === 1 ? "var(--rr-pink)" : "rgba(255,255,255,0.2)";
            document.getElementById("sim-inn1-btn").style.background = inn === 1 ? "rgba(228,28,106,0.15)" : "transparent";
            document.getElementById("sim-inn2-btn").style.borderColor = inn === 2 ? "var(--rr-pink)" : "rgba(255,255,255,0.2)";
            document.getElementById("sim-inn2-btn").style.background = inn === 2 ? "rgba(228,28,106,0.15)" : "transparent";
            document.getElementById("sim-inn-val").textContent = inn === 1 ? "1st (Setting Target)" : "2nd (Chase)";
            document.getElementById("sim-need-group").style.display = inn === 2 ? "block" : "none";
            runSimCalc();
        }}

        function resetSimDefaults() {{
            setSimInnings(2);
            document.getElementById("sim-balls").value = 12;
            document.getElementById("sim-wk").value = 5;
            document.getElementById("sim-need").value = 28;
            document.getElementById("sim-par").value = 175;
            document.getElementById("sim-elo").value = 0;
            runSimCalc();
        }}

        function runSimCalc() {{
            const bl = parseInt(document.getElementById("sim-balls").value);
            const wk = parseInt(document.getElementById("sim-wk").value);
            const need = parseInt(document.getElementById("sim-need").value);
            const par = parseInt(document.getElementById("sim-par").value);
            const elo = parseInt(document.getElementById("sim-elo").value);

            document.getElementById("sim-balls-val").textContent = `${{bl}} balls (${{(bl/6).toFixed(1)}} overs)`;
            document.getElementById("sim-wk-val").textContent = `${{wk}} wickets down`;
            document.getElementById("sim-need-val").textContent = `${{need}} runs needed`;
            document.getElementById("sim-par-val").textContent = `${{par}} runs`;
            document.getElementById("sim-elo-val").textContent = (elo >= 0 ? "+" : "") + elo;

            let wp = 0.5;
            let li = 1.0;

            if (simInnings === 2) {{
                const rrr = (need / Math.max(bl, 1)) * 6;
                const z = -0.55 * (rrr - 9.0) - 0.25 * (wk - 4) + 0.003 * elo - 0.01 * (need - bl * 1.5);
                wp = 1 / (1 + Math.exp(-z));
                wp = Math.max(0.01, Math.min(0.99, wp));

                const closeness = 1 - Math.abs(wp - 0.5) * 2;
                const timeFactor = (120 - bl) / 120;
                li = (closeness * 2.8 + timeFactor * 1.8 + (rrr > 11 ? 1.2 : 0.4)) * 0.75;
            }} else {{
                const proj = par * (1 - wk * 0.06) + (120 - bl) * 1.4;
                const gap = proj - par;
                wp = 1 / (1 + Math.exp(-(gap / 20 + elo / 150)));
                li = 0.45 + (120 - bl) / 200 + (wk >= 5 ? 0.35 : 0.1);
            }}

            const wpPct = (wp * 100).toFixed(1);
            document.getElementById("sim-wp-display").textContent = `${{wpPct}}%`;
            document.getElementById("sim-wp-bar").style.width = `${{wpPct}}%`;
            document.getElementById("sim-li-display").textContent = li.toFixed(2);

            const isHigh = li >= 1.25;
            const banner = document.getElementById("sim-pressure-banner");
            if (isHigh) {{
                banner.className = "pressure-indicator-banner indicator-high";
                banner.innerHTML = "🔥 HIGH PRESSURE BALL (Top 20% Threshold: LI ≥ 1.25)";
            }} else {{
                banner.className = "pressure-indicator-banner indicator-ordinary";
                banner.innerHTML = "⚪ ORDINARY MATCH BALL (LI &lt; 1.25)";
            }}

            // Counterfactual swings
            const cfGrid = document.getElementById("sim-counterfactuals");
            const outcomes = [
                {{ label: "Dot Ball", shift: -0.04 * li }},
                {{ label: "Single", shift: 0.01 * li }},
                {{ label: "Boundary (4)", shift: 0.09 * li }},
                {{ label: "Six (6)", shift: 0.16 * li }},
                {{ label: "Wicket", shift: -0.22 * li }}
            ];

            cfGrid.innerHTML = outcomes.map(o => {{
                const newWp = Math.max(0, Math.min(100, (wp + o.shift) * 100)).toFixed(1);
                const diff = (o.shift * 100).toFixed(1);
                const color = o.shift >= 0 ? "#10B981" : "#EF4444";
                return `
                    <div style="background: rgba(255,255,255,0.05); padding: 0.4rem; border-radius: 6px;">
                        <div style="font-weight: 600; color: #CBD5E1;">${{o.label}}</div>
                        <div style="font-weight: 800; color: ${{color}};">${{diff >= 0 ? "+" : ""}}${{diff}}%</div>
                        <div style="font-size: 0.72rem; color: #94A3B8;">WP: ${{newWp}}%</div>
                    </div>
                `;
            }}).join("");
        }}
    </script>
</body>
</html>
'''
    with open(os.path.join(base_dir, "dashboard.html"), "w", encoding="utf-8") as f:
        f.write(html_content)
    with open(os.path.join(base_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html_content)
    print("Successfully built standalone dashboard.html and index.html with Cricketer Face Cards!")

if __name__ == "__main__":
    create_dashboard_html()
