import streamlit as st
from PyPDF2 import PdfReader
from docx import Document
from groq import Groq
from googlesearch import search
import time
from run_selenium import run_selenium
import pickle
from groq_api import Groq_API_Key
from PIL import Image

image = Image.open('logo.png')
st.logo(image, size="large")
#setting the app to be wide
st.set_page_config(page_title="Skilluminati", page_icon="logo.ico", layout="wide")
st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://img.freepik.com/premium-vector/modern-dark-blue-abstract-geometric-background-with-dark-modern-triangle-texture-elegant-website-style-vector-design_116849-1059.jpg?semt=ais_hybrid");
            background-size: cover;
            background-color: rgba(0,0,0,0.6);
            background-blend-mode: darken;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
# Define the layout of the dashboard grid

# =============================================================================
# Google search module
# search(term, num_results=10, lang='en', proxy=None, advanced=False, 
#           sleep_interval=0, timeout=5, safe='active', ssl_verify=None, region=None)
# =============================================================================
#TODO: drop down box, textboxes etc are all editable for the user, we need to disable it

client = Groq(api_key=Groq_API_Key)

st.write('<style>div.block-container{padding-top:0rem;}</style>', unsafe_allow_html=True)
hide_streamlit_style = """
            <style>
                /* Hide the Streamlit header and menu */
                header {visibility: hidden;}
                /* Optionally, hide the footer */
                .streamlit-footer {display: none;}
                /* Hide your specific div class, replace class name with the one you identified */
                .st-emotion-cache-uf99v8 {display: none;}
            </style>
            """

st.markdown(hide_streamlit_style, unsafe_allow_html=True)
# Load CSS file
with open(".streamlit/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Display the title with the custom CSS class
st.markdown('<div class="custom-title">The Skilluminati</div>', unsafe_allow_html=True)
st.divider()

#Setting the webapp into 2 columns: col1 for processing and col2 for displaying data
col1,col2 = st.columns([1,1])


#function to handle pdf content etraction
def extract_text_from_pdf(pdf_file):
    pdf_reader = PdfReader(pdf_file)
    pdf_text = ""
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        pdf_text += page.extract_text()  # Extract text from each page
    return pdf_text

#function to handle word docs (docx)
def extract_text_from_docx(docx_file):
    # Extract text from DOCX
    doc = Document(docx_file)
    docx_text = ""
    for para in doc.paragraphs:
        docx_text += para.text + "\n"
    return docx_text

with col1:
    # Upload PDF file section
    file = st.file_uploader("Enter PDF/DOCx file", type=["pdf", "docx"])

    #############################################################################3

    # Select type dropdown menu

    options = ["--Select option--", "Future Job Title", "Core Desired Skills", "Career Growth"]
    selected_option = st.selectbox("Select type(Dropdown menu)", options, disabled = False)

    job_titles = ["--Select option--"]
    job_title_file = open("job_titles.pkl", "rb")
    job_titles += pickle.load(job_title_file)
    picked_title = st.selectbox("Select Job Title", job_titles)

    # Job description/roles input
    option_content = st.text_area("Enter Job Description/Roles")

    ################################################################################

    # Extract and display content based on file type
    if file is not None and option_content: #If a file is uploaded, one of the following HAS to be implemented
        file_type = file.name.split(".")[-1]
        if file_type == "pdf":
            content = extract_text_from_pdf(file)
        elif file_type == "docx":
            content = extract_text_from_docx(file)
        else:
            content = "Unsupported file type."

        ################################################################################################################3
        # Make a request to the chat completions endpoint
        if selected_option=="Core Desired Skills":
            extracted = client.chat.completions.create(
                model="llama3-70b-8192",
                seed = 20,
                messages=[
                    {"role": "user", 
                    "content": f"""Extract relevant technical skills, programming languages, and skills as specific keywords
                    they gained from the projects (name them next to the skill highlighted) that 
                    they've worked on from the text found below:\n{content}\nDo not write any paragraphs"""}
                ]
            )
            ex=extracted.choices[0].message.content
            gaps = client.chat.completions.create(
                model="llama3-70b-8192",
                messages=[
                    {"role": "user", 
                    "content": f"""Start your response with 'Skill Gaps:'. Compare these existing skills that the user has:\n {ex} \n 
                    and compare it against the core skills the user wants to enhance or develop: 
                        \n{option_content} \n and list the skill gaps as specific keywords\nDo not write any paragraphs"""}
                ]
            )
            ga=gaps.choices[0].message.content
        
        elif selected_option=="Future Job Title":
            extracted = client.chat.completions.create(
                seed = 20,
                model="llama3-70b-8192",
                messages=[
                    {"role": "user", 
                    "content": f"""Extract relevant technical skills, programming languages, and skills as specific keywords
                    they gained from the projects (name them next to the skill highlighted) that they've worked on from the text found below: 
                        \n{content}\nDo not write any paragraphs"""}
                ]
            )
            ex=extracted.choices[0].message.content
            gaps = client.chat.completions.create(
                model="llama3-70b-8192",
                messages=[
                    {"role": "user", 
                    "content": f"""Start your response with 'Skill Gaps:'. Compare these existing skills that the user has:\n. {ex} \n 
                    and compare it against the job title that the user desires: 
                        \n{option_content} \n and list the skill gaps as specific keywords\nDo not write any paragraphs"""}
                ]
            )
            ga=gaps.choices[0].message.content
        
        elif selected_option=="Career Growth":
            extracted = client.chat.completions.create(
                model="llama3-70b-8192",
                seed = 20,
                messages=[
                    {"role": "user", "content": f"""Extract relevant technical skills, programming languages, and skills as specific keywords 
                    they gained from the projects (name them next tothe skill highlighted) that they've worked on from the text found below: 
                        \n{content}\nDo not write any paragraphs"""}
                ]
            )
            ex=extracted.choices[0].message.content
            gaps = client.chat.completions.create(
                model="llama3-70b-8192",
                messages=[
                    {"role": "user", "content": f"""Start your response with the title Skill Gaps. Compare these existing skills that the user has:\n. {ex} \n
                    and compare it against the skills required by the job growth desired by the user below: 
                            \n\n{option_content} \n and list the skill gaps as specific keywords\nDo not write any paragraphs"""}
                ]
            )
            ga=gaps.choices[0].message.content
        else:
            pass
        
        resp = f"{ex} \n\n\n {ga}"
    ####################################################################################################################

    web_list=""
    gen_button = st.button("Generate")
    # Generate button
    if gen_button:
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        # Add your function here for when the button is clicked
        with st.spinner("Processing..."):
                # Simulate a processing loop
            for i in range(100):
                # Update the progress bar
                progress_bar.progress(i + 1)
                status_text.text(f"Processing... {i + 1}%")
                
                # Simulate some processing time
                time.sleep(0.07)  # Adjust the sleep time to control speed
            # Finalize when done

            search_results= search(f'Courses, datacamp, kaggle, coursera, udemy, freecodecamp, w3schools, aws skill builder: Courses for these skills: {ga}', advanced=True, num_results=10)
            for i in search_results:
                web_list+=i.url + " : " + i.description + "\n"
            
            groq_resp = client.chat.completions.create(
                model="llama3-70b-8192",
                seed = 25,
                messages=[{"role":"user",
                        "content": f"""You are a print statement and should not act like a chatbot having an interaction. you are to act like a print
                        statement printing out only the necessary data. you are helping me filter out genuine course links 
                        and scrape the others out without bothering to mention about it to me. Here are some course links and descriptions to deveop 
                        my lacking skills, 
                        write some lines describing each course: \n {web_list}\n

                        You will start with the heading: "Helpful courses" as a markdown title,
                            and links are to be generated on the NEXT LINE. Do not display to me those links that don't look like links to genuine courses to you.Don't even talk about it. Simply add description next to the link
                        in 1-2 sentences. then go to the next link on a *NEW LINE* and repeat.
                        Provided below is a thought process for you and should not be displayed by you.
                        <thought>
                        [think aboout the problem with a chain of thought]
                        </thought>

                        <response>
                        [respond as requested above without irrelevant links]
                        </response>
                        
                        look at example below:
                        Example:
                        Question:
                        <links>
                        [insert example links]
                        </links>
                        
                        Answer:
                        <thought>
                            [insert thought]
                        </thought>

                        <response>
                            [insert response.every link on a brand new line. Only print this part, dont look like an xml doc]
                        </response>


                        After you are done with this, write a heading "Project Ideas" as a markdown title. Our next mission is to provide relevant project ideas to help the user upskill. the projects should be from an 
                        easy level 1 project, moderate level 2 project, and a difficult level 3 project (3 projects in total).
                        """
                        }])
            stre_n_weak = client.chat.completions.create(
                    model="llama3-70b-8192",
                    seed = 25,
                    messages=[{"role":"user",
                            "content": f"""
                            Based on the extracted keywords from my resume: {ex}\n
                            and skill gaps that I have: {ga}\n write abount my strengths first
                            then weaknesses in bullet points. Write the headings of the lists as "Techinal Strengths" and "Areas to Improve on" as markdown titles
                            """
                            }])
            status_text.text("Done!")
            st.success("Processing completed!")

            st.write(stre_n_weak.choices[0].message.content+"\n\n"+groq_resp.choices[0].message.content)

with col2:
    if gen_button:
        tables, maps= run_selenium(picked_title)
        for i, table_sel in enumerate(tables):
            if i!=1 and i!=2: 
                continue
            table = table_sel.get_attribute("outerHTML")
            st.markdown(table, unsafe_allow_html=True)
        for i, img_sel in enumerate(maps):
            if False: 
                continue
            img = img_sel.get_attribute("src")
            if "current" not in img:
                continue
            if "sw" in img or "se" in img:
                st.image(img)
    
st.divider()
# Display footer or additional content as needed
st.write(" ")
