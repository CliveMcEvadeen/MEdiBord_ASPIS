from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from .views import upload_file, upload_success

from . import views
# # import debug_toolbar

urlpatterns_1 = [
  path(''       , views.index,  name='index'),
  path('tables/', views.tables, name='tables'),
]

    # path("student_class/", views.student_class, name="student_class"),
    # path("student_list/", views.student_list, name="student_list"),


context={
    "page":"login",
    "page_title":"Login",
    "system_name": views.context["system_name"],
    "short_name":views.context["short_name"],
    "has_navigation":False,
    "has_sidebar":False,
}
urlpatterns = [
#     path(''       , views.index,  name='index'),
#     path('tables/', views.tables, name='tables'),

    path("redirect-admin", RedirectView.as_view(url="/admin"),name="redirect-admin"),
    path("login",auth_views.LoginView.as_view(template_name="login.html",redirect_authenticated_user = True,extra_context = context),name="login"),
    path("logout",views.logoutuser,name="logout"),
    path("userlogin", views.login_user, name="login-user"),
    path("profile", views.profile, name="profile-page"),
    path("update_profile", views.update_profile, name="update-profile"),
    path("update_password", views.update_password, name="update-password"),
    path("class_mgt", views.class_mgt,name="class-page"),
    path("manage_class", views.manage_class,name="manage-class"),
    path("manage_class/<int:pk>", views.manage_class,name="manage-class-pk"),
    path("save_class", views.save_class,name="save-class"),
    path("delete_class", views.delete_class,name="delete-class"),
    path("subject_mgt", views.subject_mgt,name="subject-page"),
    path("manage_subject", views.manage_subject,name="manage-subject"),
    path("manage_subject/<int:pk>", views.manage_subject,name="manage-subject-pk"),
    path("view_subject/<int:pk>", views.view_subject,name="view-subject-pk"),
    path("save_subject", views.save_subject,name="save-subject"),
    path("delete_subject", views.delete_subject,name="delete-subject"),
    path("student", views.student_mgt,name="student-page"),
    path("manage_student", views.manage_student,name="manage-student"),
    path("manage_student/<int:pk>", views.manage_student,name="manage-student-pk"),
    path("view_student/<int:pk>", views.view_student,name="view-student-pk"),
    path("save_student", views.save_student,name="save-student"),
    path("delete_student", views.delete_student,name="delete-student"),
    path("result", views.result_mgt,name="result-page"),
    path("manage_result", views.manage_result,name="manage-result"),
    path("manage_result/<int:pk>", views.manage_result,name="manage-result-pk"),
    path("view_result/<int:pk>", views.view_result,name="view-result-pk"),
    path("save_result", views.save_result,name="save-result"),
    path("delete_result", views.delete_result,name="delete-result"),
    path("select_student", views.select_student,name="select-student"),
    path("list_result", views.list_student_result,name="list-result"),
    path("create_subject_detail/", views.add_subject_detail, name="create_subject_detail"),
    path("list_result/<int:pk>", views.list_student_result),
    path("submission_form/", views.physics_form, name="physics_form"),
    path("subjects/", views.subjects, name="subjects"),
    path("subjects_form_view/", views.subjects_form_view, name="subjects_form_view"),
    path("student_mgt/", views.student_mgt, name="student_mgt"),
    path("copy-sheet/", views.copy_sheet_to_desktop, name="copy_sheet_to_desktop"),
    path("class_list/", views.student_class_list, name="student_class_list"),
    path("data_list/", views.data_list, name="data_list"),
    path("isolated_classes/", views.isolated_classes, name="isolated_classes"),
    path('filter-students/', views.filter_students, name='filter_students'),
    path('return_home/', views.return_home, name='return_home'),
    path('view_sheet/', views.view_sheet, name='view_sheet'),
    # path("create_bar_chart/", views.create_bar_chart, name="create_bar_chart"),
    # path("generate_chart_image/", views.generate_chart_image, name="generate_chart_image"),
    # # path("generate_bar_chart_image/", views.generate_bar_chart_image, name="bar_chart_image"),
    # path("generate_bar_chart_image/", views.generate_bar_chart_image, name="bar_chart_image"),
    path('all_fields_filled_checker/<int:subject_id>/<int:student_id>', views.all_fields_filled_checker, name='all_fields_filled_checker'),
    path('get_records', views.get_records, name='get_records'),
    path('excell_to_db_var', views.excell_to_db_var, name='excell_to_db_var'),
    path('combine_records', views.combine_records, name='combine_records'),
    path('student_record', views.student_record, name='student_record'),
    path('upload/', upload_file, name='upload_file'),
    path('upload/success/', upload_success, name='upload_success'),
    
    # path("__debug__/", include("debug_toolbar.urls")),
]
# + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=urlpatterns_1
