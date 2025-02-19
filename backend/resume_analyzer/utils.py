def read_resume_file(file):
    """
    Reads the content of a resume file and returns it as a string.
    """
    return file.read().decode('utf-8')

def save_analysis_results(resume, analysis_results):
    """
    Saves the analysis results to the resume instance.
    """
    resume.analysis_results = analysis_results
    resume.save()
