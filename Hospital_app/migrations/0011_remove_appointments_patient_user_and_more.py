import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


def copy_patient_user(apps, schema_editor):
    Appointment = apps.get_model("Hospital_app", "appointments")

    for appointment in Appointment.objects.all():
        if appointment.patient_user_id:
            appointment.patient_new_id = appointment.patient_user_id
            appointment.save(update_fields=["patient_new"])


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital_app', '0010_appointments_patient_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='appointments',
            name='patient_new',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                null=True,
                blank=True,
            ),
        ),

        migrations.RunPython(copy_patient_user),

        migrations.RemoveField(
            model_name='appointments',
            name='patient',
        ),

        migrations.RemoveField(
            model_name='appointments',
            name='patient_user',
        ),

        migrations.RenameField(
            model_name='appointments',
            old_name='patient_new',
            new_name='patient',
        ),
    ]