## Inspiration
We believe every individual has untapped potential waiting to be unlocked. As college students navigating the internship search, we relied on countless resources to understand the job market. This experience sparked our vision: to create an I based, one-stop platform that empowers everyone—from students to executives—to make informed career decisions and stay ahead in their professional journey.

## What it does
Skilluminati analyzes your resume using AI, quickly comparing your current skills and expertise with your career goals. It identifies skill gaps and provides curated resources to help you upskill, earn certifications, and work on real-world projects of varying difficulty. Additionally, Skilluminati offers insights into current industry wages for your target job title and provides data on job demand across different sectors in the United States.

## How we built it
We leveraged advanced **large language models (LLMs) like Llama** combined with **Retrieval-Augmented Generation (RAG)** to deeply analyze user profiles and perform precise keyword extraction. Using a robust **search engine**, we then identified the best resources to support upskilling. The final piece of Skilluminati's architecture involves Selenium to efficiently extract real-time data on job wages, job availability, and industry concentration across the United States.

## Challenges we ran into
One of the key challenges we faced was sourcing free APIs to retrieve comprehensive job analytics data from relevant websites. To overcome this, we combined search engine queries with web scraping techniques. Another obstacle was enhancing the user interface, as Streamlit's capabilities were somewhat limited in providing diverse customization options. Balancing the right mix of resources to make Skilluminati function seamlessly was one of our toughest challenges, but we successfully navigated these hurdles with persistence and ingenuity.

## Accomplishments that we're proud of
We are proud to have brought Skilluminati to life, overcoming significant limitations with available APIs. Groq, an AI chat tool was instrumental in helping us reach our goal. We’re especially proud of successfully mapping target job roles to relevant data, along with curated skill enhancement resources. Integrating and threading various components to work in harmony presented its challenges, but our persistence and problem-solving approach allowed us to overcome them.

## What we learned
Throughout the development of Skilluminati, we learned to optimize our efforts and deliver results within tight timelines. We gained valuable experience in efficient team collaboration, the importance of pair programming, and web scraping techniques. We also integrated search engines and large language models (LLMs) to enhance functionality. This project provided us with hands-on insights into implementing AI tools, empowering us to pursue even greater goals moving forward.

## What's next for The Skilluminati 
Next, we aim to fine-tune our upskilling resource recommendation system and gather even more actionable insights on job roles and availability. Additionally, we plan to integrate links to relevant job postings and GitHub resources to further enhance the platform’s value for users.
