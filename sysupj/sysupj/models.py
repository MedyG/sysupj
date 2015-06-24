# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Student(models.Model):
    sid = models.AutoField(primary_key=True)
    sname = models.TextField()
    spwd = models.TextField()
    def __unicode__(self):
	    return self.sname
    class Meta:
        db_table = u'student'

class Course(models.Model):
    cid = models.AutoField(primary_key=True)
    cname = models.TextField()
    classroom = models.TextField()
    capasity = models.IntegerField()
    coursecredit = models.IntegerField(null=True, db_column='courseCredit', blank=True) # Field name made lowercase.
    brief = models.TextField(blank=True)
    def __unicode__(self):
	    return self.cname
    class Meta:
        db_table = u'course'

class Teacher(models.Model):
    tid = models.AutoField(primary_key=True)
    tname = models.TextField()
    brief = models.TextField(blank=True)
    def __unicode__(self):
	    return self.tname
    class Meta:
        db_table = u'teacher'

class Discussion(models.Model):
    did = models.AutoField(primary_key=True)
    poster = models.ForeignKey(Student, db_column='poster')
    #poster = models.IntegerField()
    dtype = models.IntegerField()
    #target = models.ForeignKey(Course, null=True, db_column='target', blank=True)
    target = models.IntegerField()
    content = models.TextField(blank=True)
    def __unicode__(self):
	    return self.content
    class Meta:
        db_table = u'discussion'

class Followings(models.Model):
    id = models.AutoField(primary_key=True)
    follower = models.ForeignKey(Student, null=True, db_column='follower', blank=True)
    followee = models.ForeignKey(Course, null=True, db_column='followee', blank=True)
    class Meta:
        db_table = u'followings'

class Material(models.Model):
    mid = models.AutoField(primary_key=True)
    uploader = models.ForeignKey(Student, db_column='uploader')
    course = models.ForeignKey(Course, db_column='course')
    filepath = models.TextField()
    name = models.TextField()
    class Meta:
        db_table = u'material'

class Rating(models.Model):
    rid = models.AutoField(primary_key=True)
    rater = models.ForeignKey(Student, db_column='rater')
    target = models.ForeignKey(Teacher, db_column='target')
    rating = models.IntegerField()
    class Meta:
        db_table = u'rating'

class Teachings(models.Model):
    id = models.AutoField(primary_key=True)
    teacher = models.ForeignKey(Teacher, db_column='teacher')
    course = models.ForeignKey(Course, db_column='course')
    class Meta:
        db_table = u'teachings'

