import streamlit as st
from datetime import date

# ---------- Page config ----------
st.set_page_config(
    page_title="Prompt My Papers",
    page_icon="📝",
    layout="centered",
)
st.title("📝 Prompt My Papers")
st.caption("Generate high‑quality ChatGPT prompts for essays and research papers—no API or paid plan required.")

# ---------- Sidebar: user inputs ----------
with st.sidebar:
    st.header("🔧 Configure Your Essay")

    topic = st.text_input("Essay topic", placeholder="e.g. Impact of social media on teenagers")

    essay_type = st.selectbox(
        "Essay type",
        [
            "Analytical",
            "Argumentative",
            "Persuasive",
            "Narrative",
            "Compare & Contrast",
            "Cause & Effect",
            "Expository",
        ],
    )

    word_count = st.number_input(
        "Desired word count",
        min_value=250,
        max_value=5000,
        step=50,
        value=1000,
    )

    academic_level = st.selectbox(
        "Academic level",
        ["High School", "Undergraduate", "Master’s", "PhD"],
    )

    writing_style = st.selectbox(
        "Writing style / tone",
        ["Formal Academic", "Conversational Academic", "Creative", "Technical"],
    )

    urgency = st.slider(
        "Days until deadline",
        min_value=1,
        max_value=30,
        value=7,
        help="Helps tailor the research depth and time‑management tips.",
    )

    show_introduction = st.checkbox("Include a sample introduction paragraph", value=True)
    show_sources      = st.checkbox("Include suggested source types", value=True)
    show_citations    = st.checkbox("Recommend citation style", value=True)

# ---------- Generate prompt ----------
st.subheader("✍️ Your ChatGPT Prompt")

if st.button("Generate Prompt", type="primary"):

    if not topic.strip():
        st.error("Please enter an essay topic in the sidebar first.")
        st.stop()

    # Build the prompt step‑by‑step
    prompt_lines = [
        f"Act as an academic writing coach.",
        f"I’m writing a **{word_count}-word {essay_type.lower()} essay** at **{academic_level}** level.",
        f"**Topic:** \"{topic}\"",
        f"**Writing style:** {writing_style}",
        f"My deadline is in **{urgency} days**.",
        "",
        "Please provide:",
        "1. A detailed essay outline with 3–5 main sections and bullet‑point sub‑arguments.",
        "2. A clear thesis statement.",
    ]

    line_no = 3  # keeps numbering consistent if options drop
    if show_introduction:
        line_no += 1
        prompt_lines.append(f"{line_no}. A sample introduction paragraph (100–150 words).")
    if show_sources:
        line_no += 1
        prompt_lines.append(f"{line_no}. Suggestions for reputable sources or study types to reference.")
    if show_citations:
        line_no += 1
        prompt_lines.append(f"{line_no}. The appropriate citation style (explain why it suits this assignment).")

    prompt_lines.append("")
    prompt_lines.append("Keep the tone and vocabulary appropriate for the stated academic level.")

    full_prompt = "\n".join(prompt_lines)

    # Show prompt inside a text area (auto‑select for easy copy)
    st.text_area(
        label="Copy & paste this into ChatGPT (Free) 👇",
        value=full_prompt,
        height=350,
    )

    # Optional: offer download as .txt
    file_name = f"PromptMyPapers_{date.today().isoformat()}.txt"
    st.download_button(
        label="💾 Download as .txt",
        data=full_prompt,
        file_name=file_name,
        mime="text/plain",
    )

    st.success("Prompt generated! Paste it into ChatGPT and watch the magic. ✨")
else:
    st.info("Use the sidebar to configure your essay, then click **Generate Prompt**.")

# ---------- Footer ----------
st.markdown(
    """
    <hr/>
    <p style='text-align:center; font-size:0.9em;'>
        iKronyx with ❤️ using <a href='https://streamlit.io' target='_blank'>Streamlit</a> •
        Last updated {today}
    </p>
    """.format(today=date.today().strftime("%b %d, %Y")),
    unsafe_allow_html=True,
)
