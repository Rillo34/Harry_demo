# from uuid import uuid4
# from nicegui import ui
# import random
# from typing import List
# from pydantic import BaseModel, Field, computed_field, field_serializer
# from typing import List, Optional, Literal
# from datetime import date, datetime

# class JobCandidateScore(BaseModel):
#     job_id: str = Field(default_factory=lambda: uuid4().hex[:5])
#     candidate_id: str = Field(description="The unique ID of the candidate being evaluated for the job.")
#     comp_score: Optional[float] = Field(default=None, description="The combined score for the candidate in relation to the job, calculated based on requirements and availability.")
#     comp_summary: Optional[str] = Field(default=None, description="A brief summary of the candidate's fit for the job, highlighting key strengths or concerns based on the requirements and availability.")
#     availability_score: Optional[float] = Field(default=None, description="A score from 1-10 indicating the candidate's availability for the job, where 10 means fully available and 1 means not available at all.")
#     avail_summary: Optional[str] = Field(default=None, description="A brief summary of the candidate's availability, including any potential conflicts or constraints that may affect their suitability for the job.")



# def generate_random_candidate_job_scores(
#     candidates: List[str],
#     jobs: List[str]
# ) -> List[JobCandidateScore]:
#     results = []

#     for candidate_id in candidates:
#         for job_id in jobs:

#             comp_score = round(random.uniform(1, 100), 0 )
#             availability_score = round(random.uniform(1, 100), 0)

#             comp_summary = (
#                 f"Kandidaten matchar rollen på en nivå av {comp_score}/10."
#                 if comp_score > 6 else
#                 f"Kandidaten har vissa luckor i matchningen ({comp_score}/10)."
#             )

#             avail_summary = (
#                 f"Tillgängligheten är god ({availability_score}/10)."
#                 if availability_score > 6 else
#                 f"Tillgängligheten är begränsad ({availability_score}/10)."
#             )

#             score = JobCandidateScore(
#                 job_id=job_id,
#                 candidate_id=candidate_id,
#                 comp_score=comp_score,
#                 comp_summary=comp_summary,
#                 availability_score=availability_score,
#                 avail_summary=avail_summary
#             )

#             results.append(score)

#     return results

# import pandas as pd
# import random
# from typing import List

# def generate_scores_df(
#     candidates: List[str],
#     jobs: List[str]
# ) -> pd.DataFrame:

#     rows = []

#     for candidate_id in candidates:
#         for job_id in jobs:

#             comp_score = round(random.uniform(1, 100), 0)
#             availability_score = round(random.uniform(1, 100), 0)

#             comp_summary = (
#                 f"Kandidaten matchar rollen på en nivå av {comp_score}/10."
#                 if comp_score > 60 else
#                 f"Kandidaten har vissa luckor i matchningen ({comp_score}/10)."
#             )

#             avail_summary = (
#                 f"Tillgängligheten är god ({availability_score}/10)."
#                 if availability_score > 60 else
#                 f"Tillgängligheten är begränsad ({availability_score}/10)."
#             )

#             rows.append({
#                 "candidate_id": candidate_id,
#                 "job_id": job_id,
#                 "comp_score": comp_score,
#                 "availability_score": availability_score,
#                 "comp_summary": comp_summary,
#                 "avail_summary": avail_summary,
#             })

#     df = pd.DataFrame(rows)

#     # 🔥 bonus: total score direkt
#     # df["total_score"] = 0.7 * df["comp_score"] + 0.3 * df["availability_score"]

#     return df

# def score_color(score: float) -> str:
#     if score >= 90:
#         return 'EXCELLENT'
#     elif score >= 70:
#         return 'WITH SHUFFLE'
#     elif score >= 50:
#         return 'OK'
#     elif score >= 30:
#         return 'WEAK'
#     else:
#         return 'BAD'
# color_map = {
#         'OK': '#2ecc71',
#         'BAD': '#e74c3c',
#         'WEAK': '#f39c12',
#         'EXCELLENT': '#3498db',
#         'WITH SHUFFLE': '#95a5a6'
#     }


# candidates = [
#     "Anna Bergström",
#     "Johan Lindqvist",
#     "Sara Ekholm",
#     "Marcus Dahl",
#     "Elin Forsberg",
#     "Daniel Nyström",
#     "Karin Sjöberg",
#     "Oskar Håkansson",
#     "Linda Wallin",
#     "Patrik Holmgren",
# ]

# jobs = [
#     "job_001",
#     "job_002",
#     "job_003",
#     "job_004",
#     "job_005",
#     "job_006",
#     "job_007",
#     "job_008",
#     "job_009",
#     "job_010",
# ]

# results = generate_random_candidate_job_scores(candidates, jobs)

# results_df = generate_scores_df(candidates, jobs)
# print(results_df[["candidate_id", "job_id", "comp_score", "availability_score"]].head())


# def get_sorted_candidates(df, job_id, metric="comp_score"):
#     return (
#         df[df.job_id == job_id]
#         .sort_values(metric, ascending=False)['candidate_id']
#         .tolist()
#     )

# def render_grid(
#     df,
#     sort_job=None,
#     sort_candidate=None,
#     sort_metric="comp_score"
# ):
#     container = ui.column().classes('gap-2')
#     container.clear()

#     jobs = list(df['job_id'].unique())
#     candidates = list(df['candidate_id'].unique())

#     pivot = df.set_index(['candidate_id', 'job_id'])

#     # 🔥 SORT: candidates baserat på job
#     if sort_job:
#         sorted_df = (
#             df[df.job_id == sort_job]
#             .sort_values(sort_metric, ascending=False)
#         )
#         candidates = sorted_df['candidate_id'].tolist()

#     # 🔥 SORT: jobs baserat på candidate
#     if sort_candidate:
#         sorted_jobs = (
#             df[df.candidate_id == sort_candidate]
#             .sort_values(sort_metric, ascending=False)
#         )
#         jobs = sorted_jobs['job_id'].tolist()

#     focus_job = sort_job
#     focus_candidate = sort_candidate
#     container = ui.column().classes('gap-2')
#     with container:
#         with ui.grid(columns=len(jobs) + 1).classes('gap-1'):

#             # 🔝 HEADER
#             ui.label('')

#             for job in jobs:
#                 cls = "font-bold text-center w-24"

#                 if focus_job and job == focus_job:
#                     cls += " ring-2 ring-blue-500 bg-white"
#                 elif focus_job:
#                     cls += " opacity-40"

#                 ui.label(job).classes(cls)

#             # 🔽 ROWS
#             for cand in candidates:

#                 cls = "font-bold w-32 text-center"

#                 if focus_candidate and cand == focus_candidate:
#                     cls += " ring-2 ring-blue-500 bg-white"
#                 elif focus_candidate:
#                     cls += " opacity-40"

#                 ui.label(cand).classes(cls)

#                 for job in jobs:

#                     row = pivot.loc[(cand, job)]

#                     comp_color = color_map.get(
#                         score_color(row.comp_score),
#                         'bg-gray-200'
#                     )

#                     avail_color = color_map.get(
#                         score_color(row.availability_score),
#                         'bg-gray-200'
#                     )

#                     cell_cls = "p-0 w-24 h-10 shadow-sm"

#                     # 🔥 DIM CELLS om fokus finns
#                     if focus_job and job != focus_job:
#                         cell_cls += " opacity-40"
#                     if focus_candidate and cand != focus_candidate:
#                         cell_cls += " opacity-40"

#                     with ui.card().classes(cell_cls):
#                         with ui.element('div').classes('flex w-full h-full'):

#                             with ui.element('div') \
#                                 .style(f'background-color: {comp_color};') \
#                                 .classes('flex-1 flex items-center justify-center'):

#                                 ui.label(str(int(row.comp_score))) \
#                                     .classes('text-white text-sm font-bold')

#                             with ui.element('div') \
#                                 .style(f'background-color: {avail_color};') \
#                                 .classes('flex-1 flex items-center justify-center'):

#                                 ui.label(str(int(row.availability_score))) \
#                                     .classes('text-black text-sm font-bold')

# @ui.page("/")
# def index():
#     ui.label("Job–Candidate Matrix (10×10)").classes('text-2xl font-bold mb-4')
#     ui.label(f"Total: {len(results)}").classes('mb-4')

#     # Header-rad: tom cell + kandidater
#     with ui.row().classes('items-center gap-2 mb-2'):
#         ui.label("").classes('w-32')  # tom hörncell
#         for cand in candidates:
#             ui.label(cand).classes('font-bold w-32 text-center')

#     # Grid: en rad per jobb
#     for job in jobs:
#         with ui.row().classes('items-start gap-2'):
#             # Vänsterkolumn: jobbtitel
#             ui.label(job).classes('font-bold w-32')
#             i=0
#             # 10 celler för varje kandidat
#             for cand in candidates:
#                 i+=1
#                 # hitta rätt result (robust matchning)
#                 r = next(
#                     (x for x in results if x.job_id == job and x.candidate_id == cand),
#                     None
#                 )
#                 comp_color = score_color(r.comp_score) if r and r.comp_score is not None else 'bg-gray-200'
#                 comp_color = color_map.get(comp_color, 'bg-gray-200')
#                 # print(f"Comp color: {comp_color} baserat på comp_score: {r.comp_score if r else 'N/A'}")
#                 # if i==1:
#                 #     print(f"För jobb {job} och kandidat {cand} hittades resultat: {r}")
#                 #     print (f"Comp color: {comp_color} baserat på comp_score: {r.comp_score if r else 'N/A'}")
#                 avail_color = score_color(r.availability_score) if r and r.availability_score is not None else 'bg-gray-200'
#                 # print(f"Availability color: {avail_color} baserat på availability_score: {r.availability_score if r else 'N/A'}")
#                 avail_color = color_map.get(avail_color, 'bg-gray-200')
#                 # print(f"Mapped availability color: {avail_color}")
#                 if r is None:
#                     with ui.card().classes('p-0 w-32 h-10'):
#                         ui.label("Missing").classes("text-red-600")
#                     continue

#                 with ui.card().classes('p-0 w-32 h-10'):
#                     with ui.row().classes('w-full h-full no-wrap gap-0'):
#                         with ui.element('div').style(f'background-color: {comp_color};').classes('w-1/2 h-full flex items-center justify-center'):
#                             ui.label(f'{r.comp_score}').classes('text-white font-bold')

#                         with ui.element('div').style(f'background-color: {avail_color};').classes('w-1/2 h-full flex items-center justify-center'):
#                             label =ui.label(f'{r.availability_score}').classes('text-black font-bold')
#                             with label:
#                                 ui.tooltip(r.avail_summary).classes('text-sm')
#     ui.label('Hover me').tooltip('Detta är texten som visas vid hover')

#     render_grid(results_df)
#     render_grid(results_df, sort_job="job_001", sort_metric="comp_score")
#     render_grid(results_df, sort_candidate="Karin Sjöberg", sort_metric="comp_score")                                
# # ui.run(port=8003)
