import streamlit as st

st.set_page_config(
    page_title="Incentivos Coppel",
    page_icon="🏆",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
.stApp { background-color: #F0F4FF; font-family: 'Segoe UI', sans-serif; }
.header-coppel {
    background: linear-gradient(135deg, #003DA5, #0056D6);
    padding: 20px; border-radius: 16px; text-align: center;
    margin-bottom: 20px; box-shadow: 0 4px 12px rgba(0,61,165,0.3);
}
.header-coppel h1 { font-size: 1.6em; margin: 0; color: #FFD100 !important; }
.header-coppel p  { margin: 5px 0 0 0; font-size: 0.95em; color: white; }
.seccion-card {
    background: white; border-radius: 16px; padding: 20px;
    margin-bottom: 16px; border-left: 5px solid #003DA5;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}
.seccion-titulo { color: #003DA5; font-size: 1.1em; font-weight: bold; margin-bottom: 4px; }
.divider-azul { border: none; border-top: 1.5px solid #003DA5; opacity: 0.2; margin: 10px 0 14px 0; }
.resultado-card {
    background: linear-gradient(135deg, #003DA5, #0056D6);
    border-radius: 16px; padding: 24px; text-align: center;
    color: white; margin-top: 20px; box-shadow: 0 6px 20px rgba(0,61,165,0.4);
}
.resultado-total { font-size: 2.5em; font-weight: bold; color: #FFD100; }
.resultado-label { font-size: 1em; color: white; margin-bottom: 8px; }
.metrica-box { background: #E8F0FF; border-radius: 12px; padding: 12px; text-align: center; margin: 8px 0; }
.metrica-valor { font-size: 1.4em; font-weight: bold; color: #003DA5; }
.metrica-etiqueta { font-size: 0.8em; color: #555; }
.chip-verde    { background-color: #D4EDDA; color: #155724; border-radius: 20px; padding: 4px 12px; font-size: 0.85em; display: inline-block; margin: 4px 0; }
.chip-rojo     { background-color: #F8D7DA; color: #721C24; border-radius: 20px; padding: 4px 12px; font-size: 0.85em; display: inline-block; margin: 4px 0; }
.chip-amarillo { background-color: #FFF3CD; color: #856404; border-radius: 20px; padding: 4px 12px; font-size: 0.85em; display: inline-block; margin: 4px 0; }
[data-testid="stSidebar"] { background-color: #003DA5 !important; }
[data-testid="stSidebar"] * { color: white !important; }
#MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ── HELPERS ─────────────────────────────────────────────
def card_open(titulo):
    st.markdown(f'''<div class="seccion-card">
        <div class="seccion-titulo">{titulo}</div>
        <hr class="divider-azul">''', unsafe_allow_html=True)

def card_close():
    st.markdown('</div>', unsafe_allow_html=True)

def metrica(etiqueta, valor):
    st.markdown(f'''<div class="metrica-box">
        <div class="metrica-etiqueta">{etiqueta}</div>
        <div class="metrica-valor">{valor}</div>
    </div>''', unsafe_allow_html=True)

def chip(tipo, texto):
    st.markdown(f'<span class="chip-{tipo}">{texto}</span>', unsafe_allow_html=True)

def resultado_final(total, desglose):
    st.markdown(f'''<div class="resultado-card">
        <div class="resultado-label">🏆 TU INCENTIVO TOTAL DEL MES</div>
        <div class="resultado-total">${total:,.2f}</div>
        <br>
        <div style="font-size:0.85em; color:#cce0ff;">{desglose}</div>
    </div>''', unsafe_allow_html=True)

def incentivo_base_asesor(cump):
    if cump < 85:    return 0
    elif cump < 95:  return 700
    elif cump < 100: return 850
    elif cump < 110: return 1150
    elif cump < 120: return 1400
    else:            return 1750

def seccion_comisiones_asesor(cump_equipo, prefix):
    pct_s, pct_m = (0.04, 0.006) if cump_equipo >= 100 else (0.015, 0.004)
    if cump_equipo >= 100:
        chip("verde",    "✅ Tasas Cump ≥ 100%: Seguros/Servicios 4% | Marketplace 0.6%")
    else:
        chip("amarillo", "⚠️ Tasas Cump < 100%: Seguros/Servicios 1.5% | Marketplace 0.4%")
    st.markdown('<hr class="divider-azul">', unsafe_allow_html=True)
    st.markdown("**Seguros y Coppel Soluciones**")
    v_club  = st.number_input("🛡️ Seguros Club de Protección ($)",  min_value=0.0, step=100.0, format="%.2f", key=f"{prefix}_club")
    v_mrc   = st.number_input("🏍️ Seguros Motos RC ($)",            min_value=0.0, step=100.0, format="%.2f", key=f"{prefix}_mrc")
    v_mplus = st.number_input("🏍️ Seguros Motos PLUS ($)",          min_value=0.0, step=100.0, format="%.2f", key=f"{prefix}_mplus")
    v_cel   = st.number_input("📱 Seguros Celulares ($)",            min_value=0.0, step=100.0, format="%.2f", key=f"{prefix}_cel")
    v_gar   = st.number_input("🔧 Garantía Extendida ($)",           min_value=0.0, step=100.0, format="%.2f", key=f"{prefix}_gar")
    v_arm   = st.number_input("🔩 Servicio de Armado ($)",           min_value=0.0, step=100.0, format="%.2f", key=f"{prefix}_arm")
    v_inst  = st.number_input("🔌 Servicio de Instalación ($)",      min_value=0.0, step=100.0, format="%.2f", key=f"{prefix}_inst")
    st.markdown('<hr class="divider-azul">', unsafe_allow_html=True)
    st.markdown("**Marketplace y Campañas**")
    v_market = st.number_input("🛒 Venta Marketplace (3P) y Campañas ($)", min_value=0.0, step=100.0, format="%.2f", key=f"{prefix}_market")
    total_seguros  = (v_club + v_mrc + v_mplus + v_cel + v_gar + v_arm + v_inst) * pct_s
    total_market   = v_market * pct_m
    total_comision = total_seguros + total_market
    col1, col2, col3 = st.columns(3)
    with col1: metrica("🛡️ Comisión Seguros",    f"${total_seguros:,.2f}")
    with col2: metrica("🛒 Comisión Marketplace", f"${total_market:,.2f}")
    with col3: metrica("📊 Total Comisiones",     f"${total_comision:,.2f}")
    return total_comision

# ── SIDEBAR ─────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🏢 Coppel Incentivos")
    st.markdown("---")
    st.markdown("### 👤 Selecciona tu puesto:")
    puesto = st.radio("", options=[
        "🛒 Asesor de Ventas",
        "📱 Asesor Telefonía",
        "👁️ Optometrista",
        "⚙️ Operativos",
        "💰 Cajero Multifuncional",
        "👔 Gerente Titular",
    ], index=0)
    st.markdown("---")
    st.markdown("<small>Calculadora Interna Coppel v1.0</small>", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════
# FUNCIÓN GENÉRICA — ASESOR (Ventas / Telefonía / Optometrista)
# ════════════════════════════════════════════════════════
def pantalla_asesor(titulo, prefix):
    st.markdown(f'''<div class="header-coppel">
        <h1>🏆 Calculadora de Incentivos</h1>
        <p>{titulo} — Coppel</p>
    </div>''', unsafe_allow_html=True)

    card_open("🤝 Paso 1 — Venta de Equipo")
    cump_equipo = st.number_input("% Cumplimiento meta del equipo",
        min_value=0.0, max_value=200.0, step=0.01, format="%.2f", key=f"{prefix}_equipo")
    incentivo_base = incentivo_base_asesor(cump_equipo)
    if cump_equipo < 85:     chip("rojo",     "❌ < 85% — Sin incentivo base")
    elif cump_equipo < 100:  chip("amarillo", "⚠️ Cumplimiento parcial")
    else:                    chip("verde",    "✅ Meta alcanzada")
    metrica("💰 Incentivo Base", f"${incentivo_base:,.2f}")
    card_close()

    card_open("✖️ Paso 2 — Multiplicadores")
    cump_credito = st.number_input("% Cumplimiento Venta a Crédito",
        min_value=0.0, max_value=200.0, step=0.01, format="%.2f", key=f"{prefix}_credito")
    cump_digital = st.number_input("% Cumplimiento Cliente Digital Avanzado",
        min_value=0.0, max_value=200.0, step=0.01, format="%.2f", key=f"{prefix}_digital")
    multiplicador = 1.0
    if cump_credito >= 95:
        multiplicador += 0.20
        chip("verde", "✅ Venta a Crédito ≥ 95% → +0.20")
    else:
        chip("rojo",  "❌ Venta a Crédito < 95% → +0.00")
    if cump_digital >= 95:
        multiplicador += 0.15
        chip("verde", "✅ Cliente Digital ≥ 95% → +0.15")
    else:
        chip("rojo",  "❌ Cliente Digital < 95% → +0.00")
    incentivo_con_mult = incentivo_base * multiplicador
    col1, col2 = st.columns(2)
    with col1: metrica("✖️ Multiplicador",     f"×{multiplicador:.2f}")
    with col2: metrica("💰 Con Multiplicador", f"${incentivo_con_mult:,.2f}")
    card_close()

    card_open("💼 Paso 3 — Comisiones por Tipo de Venta")
    total_comisiones = seccion_comisiones_asesor(cump_equipo, prefix)
    card_close()

    card_open("🏪 Paso 4 — Bono por Venta de Tienda")
    cump_tienda = st.number_input("% Cumplimiento meta de la tienda",
        min_value=0.0, max_value=200.0, step=0.01, format="%.2f", key=f"{prefix}_tienda")
    bono_tienda = 0.0
    if cump_tienda >= 100:
        bono_tienda = 0.20
        chip("verde", "✅ Tienda ≥ 100% — Bono adicional del 20%")
    else:
        chip("rojo",  "❌ Tienda < 100% — Sin bono adicional")
    card_close()

    subtotal    = incentivo_con_mult + total_comisiones
    bono_extra  = subtotal * bono_tienda
    total_final = subtotal + bono_extra
    resultado_final(total_final,
        f"Base: ${incentivo_base:,.2f} | ×{multiplicador:.2f} = ${incentivo_con_mult:,.2f}<br>"
        f"Comisiones: ${total_comisiones:,.2f} | Bono Tienda: ${bono_extra:,.2f}")

# ════════════ PUESTOS ════════════════════
if   puesto == "🛒 Asesor de Ventas":    pantalla_asesor("Asesor de Ventas", "av")
elif puesto == "📱 Asesor Telefonía":    pantalla_asesor("Asesor Telefonía",  "at")
elif puesto == "👁️ Optometrista":        pantalla_asesor("Optometrista",      "opt")

# ════════ OPERATIVOS ═════════════════════
elif puesto == "⚙️ Operativos":
    # ... (código Operativos igual que antes)

# ════════ CAJERO MULTIFUNCIONAL ══════════
elif puesto == "💰 Cajero Multifuncional":
    # ... (código Cajero igual que antes)

# ════════ GERENTE TITULAR ════════════════
elif puesto == "👔 Gerente Titular":
    # ... (código Gerente igual que antes)

st.markdown("<br>", unsafe_allow_html=True)
st.caption("Calculadora Interna Coppel • v1.0 • Solo para uso interno")

