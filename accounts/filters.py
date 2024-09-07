from django.contrib.admin import SimpleListFilter


class EmailDomainFilter(SimpleListFilter):
    title = 'email domain'
    parameter_name = 'email_domain'

    def lookups(self, request, model_admin):
        return tuple(
            ('@' + obj.user.email.split('@')[1],) * 2 for obj in model_admin.model.objects.all()
        )

    def queryset(self, request, queryset):
        if self.value() is not None:
            return queryset.filter(user__email__endswith=self.value())
