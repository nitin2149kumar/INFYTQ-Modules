#OOPR-Assgn-20

class Applicant:
    __application_dict={'A': 0, 'B': 0, 'C': 0}
    __applicant_id_count=1000
    def __init__(self, applicant_name):
        self.__applicant_id=0
        self.__applicant_name=applicant_name
        self.__job_band=None
    def get_applicant_id(self):
        return self.__applicant_id
    def get_applicant_name(self):
        return self.__applicant_name
    def get_job_band(self):
        return self.__job_band
    @staticmethod
    def get_application_dict():
        return __application_dict
    def generate_applicant_id(self):
        self.__applicant_id=Applicant.__applicant_id_count+1
        Applicant.__applicant_id_count+=1
    def apply_for_job(self, job_band):
        if job_band in Applicant.__application_dict.keys():
            if Applicant.__application_dict[job_band]<5:
                Applicant.__application_dict[job_band]+=1
                self.generate_applicant_id()
                self.__job_band=job_band
            else:
                return -1
a= Applicant("Jack")
a.apply_for_job("B")
