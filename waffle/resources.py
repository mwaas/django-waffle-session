from import_export import resources
from waffle.models import VerifiedUser


class VerifiedUserResource(resources.ModelResource):
    class Meta:
        model = VerifiedUser
        # Exclude verified user and feature_id. Feature returns id
        exclude = ('id', 'feature_id')
        import_id_fields = ('feature', 'phone_number', 'feature__name')
        fields = ('feature', 'phone_number', 'feature__name')
        export_order = ('feature', 'phone_number', 'feature__name')
