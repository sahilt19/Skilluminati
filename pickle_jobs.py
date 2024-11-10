import pickle
job_titles = []
file = open("oes_ids.txt")
for _line in file:
    line = _line.rstrip()
    link, job, oes_id = line.split(" | ")
    job_titles.append(job)

with open("job_titles.pkl", "wb") as file:
    pickle.dump(job_titles, file)
    
# with open("job_titles.pkl", "rb") as file:
#     unpickled = pickle.load(file)

# print(type(unpickled))
# print(unpickled)