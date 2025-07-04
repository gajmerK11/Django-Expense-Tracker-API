from rest_framework import serializers
from .models import ExpenseIncome


class ExpenseIncomeSerializer(serializers.ModelSerializer):
    # Custom field to include computed total (amount + tax) in the serialized output
    total = serializers.SerializerMethodField()

    class Meta:
        model = ExpenseIncome
        fields = (
            "__all__"  # Serialize all model fields plus any extra fields (like 'total')
        )

        # Make these fields read-only so they can't be changed via API requests
        read_only_fields = ["user", "created_at", "updated_at", "total"]

    def get_total(self, obj):
        # Calculate total on the fly using the model's 'total' method/property
        return obj.total()
