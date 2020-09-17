from django.db.models.signals import m2m_changed
from django.db.models.signals import post_save
from django.dispatch import receiver
from tasks.models import TodoItem, Category, Priority
from collections import Counter
from django.db.models import Count

@receiver(m2m_changed, sender=TodoItem.category.through)
def task_cats_added(sender, instance, action, model, **kwargs):
    if action != "post_add":
        return

    # полный пересчет, код скопирован из post_remove
    cat_counter = Counter()
    for t in TodoItem.objects.all():
        for cat in t.category.all():
            cat_counter[cat.slug] += 1

    for slug, new_count in cat_counter.items():
        Category.objects.filter(slug=slug).update(todos_count=new_count)
    
# если по категории нет ни одной задачи, то обновляем и проставляем к-во нуль
    for cat in Category.objects.all():
        if cat.slug not in cat_counter.keys():              
            Category.objects.filter(slug=cat.slug).update(todos_count=0)

@receiver(m2m_changed, sender=TodoItem.category.through)
def task_cats_removed(sender, instance, action, model, **kwargs):
    if action != "post_remove":
        return

    cat_counter = Counter()
    for t in TodoItem.objects.all():
        for cat in t.category.all():
            cat_counter[cat.slug] += 1

    for slug, new_count in cat_counter.items():
        Category.objects.filter(slug=slug).update(todos_count=new_count)

# счетчик приоритетов задач
@receiver(post_save, sender=TodoItem)
def post_save_task( sender, instance, **kwargs):
    all_pr = Priority.objects.annotate(num=Count('cl_priority'))
    for pr in all_pr:
        Priority.objects.filter(pk=pr.pk).update(priority_count=pr.num)