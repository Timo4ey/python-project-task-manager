import django_filters
from .models import Tasks
from task_manager.task_status.models import TaskStatus
from task_manager.labels.models import Label
from django import forms


class F(django_filters.FilterSet):
    STATUSES_CHOICE = TaskStatus.objects.all().values_list('id', 'name')
    PERFORMER_CHOICE = [(x.id, x.username) for x in Tasks.performer.get_queryset()]
    STATUSES_TAGS = Label.objects.all().values_list('id', 'name')

    creator = django_filters.BooleanFilter(label="Только свои задачи", method='my_custom_filter',
                                           widget=forms.CheckboxInput)

    status = django_filters.ChoiceFilter(label="Статус", choices=STATUSES_CHOICE)
    labels = django_filters.ChoiceFilter(label="Метка", choices=STATUSES_TAGS)

    class Meta:
        model = Tasks
        fields = ['status', 'performer', 'labels', 'creator']

    #
    def __init__(self,  *args, **kwargs):
        super(F, self).__init__(*args, **kwargs)
        self.user_id = self.request.user.id

    def my_custom_filter(self, queryset, field, value, *args, **kwargs):
        if value:
            print(queryset)
            return queryset.filter(creator_id=self.user_id)
        return queryset
