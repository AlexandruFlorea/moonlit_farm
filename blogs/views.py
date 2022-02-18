from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.text import slugify
from blogs.models import Post


class PostList(ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_at')
    template_name = 'blogs/post_list.html'


class PostDetails(DetailView):
    model = Post
    template_name = 'blogs/post_detail.html'


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content', 'status']
    template_name = 'blogs/post_create_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)

    



class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content', ]
    template_name = 'blogs/post_update.html'


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blogs/post_confirm_delete.html'
    success_url = reverse_lazy('blogs:all')  # We have to use reverse_lazy() instead of reverse(), as the urls are not loaded when the file is imported.
