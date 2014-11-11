# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'SyncLog'
        db.create_table(u'sofabed_synclog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('user_id', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('previous_log_id', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('last_seq', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('duration', self.gf('django.db.models.fields.IntegerField')()),
            ('cases_on_phone', self.gf('django.db.models.fields.IntegerField')()),
            ('dependent_cases_on_phone', self.gf('django.db.models.fields.IntegerField')()),
            ('owner_ids_on_phone', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'sofabed', ['SyncLog'])


    def backwards(self, orm):
        
        # Deleting model 'SyncLog'
        db.delete_table(u'sofabed_synclog')


    models = {
        u'sofabed.caseactiondata': {
            'Meta': {'unique_together': "(('case', 'index'),)", 'object_name': 'CaseActionData'},
            'action_type': ('django.db.models.fields.CharField', [], {'max_length': '64', 'db_index': 'True'}),
            'case': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'actions'", 'to': u"orm['sofabed.CaseData']"}),
            'date': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index': ('django.db.models.fields.IntegerField', [], {}),
            'server_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'sync_log_id': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True'}),
            'user_id': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'db_index': 'True'}),
            'xform_id': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True'}),
            'xform_xmlns': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True'})
        },
        u'sofabed.casedata': {
            'Meta': {'object_name': 'CaseData'},
            'case_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128', 'primary_key': 'True'}),
            'closed': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'closed_by': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'db_index': 'True'}),
            'closed_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_index': 'True'}),
            'doc_type': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_index': 'True'}),
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_index': 'True'}),
            'external_id': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True'}),
            'modified_by': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'db_index': 'True'}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True'}),
            'opened_by': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'db_index': 'True'}),
            'opened_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_index': 'True'}),
            'owner_id': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'db_index': 'True'}),
            'server_modified_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_index': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'db_index': 'True'}),
            'user_id': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'db_index': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'db_index': 'True'})
        },
        u'sofabed.caseindexdata': {
            'Meta': {'object_name': 'CaseIndexData'},
            'case': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'indices'", 'to': u"orm['sofabed.CaseData']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '64', 'db_index': 'True'}),
            'referenced_id': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_index': 'True'}),
            'referenced_type': ('django.db.models.fields.CharField', [], {'max_length': '64', 'db_index': 'True'})
        },
        u'sofabed.formdata': {
            'Meta': {'object_name': 'FormData'},
            'app_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'device_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'doc_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'duration': ('django.db.models.fields.BigIntegerField', [], {}),
            'instance_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'primary_key': 'True'}),
            'received_on': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'time_end': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'time_start': ('django.db.models.fields.DateTimeField', [], {}),
            'user_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'xmlns': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'db_index': 'True'})
        },
        u'sofabed.synclog': {
            'Meta': {'object_name': 'SyncLog'},
            'cases_on_phone': ('django.db.models.fields.IntegerField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'dependent_cases_on_phone': ('django.db.models.fields.IntegerField', [], {}),
            'duration': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_seq': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'owner_ids_on_phone': ('django.db.models.fields.IntegerField', [], {}),
            'previous_log_id': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'user_id': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['sofabed']
