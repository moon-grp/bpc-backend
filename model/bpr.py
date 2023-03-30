import ssl
from typing import List
from mongoengine import Document, StringField, DecimalField, URLField, BooleanField, ObjectIdField, EmailField, IntField, DateField, BinaryField
from dotenv import load_dotenv
from mongoengine import connect, disconnect
import os
from mongoengine.document import DynamicDocument

from mongoengine.fields import ListField
load_dotenv()


uri = os.getenv("db_connection")


connect(host=uri, alias="default", ssl_cert_reqs=ssl.CERT_NONE)



class BxdApprl(DynamicDocument):
    name: StringField()
    empId: StringField()
    workOutput: IntField()
    domainKnowledge: IntField()
    softSkils: IntField()
    domainSkills: IntField()
    onThejob: IntField()
    workValues: IntField()
    finalScore: IntField()
