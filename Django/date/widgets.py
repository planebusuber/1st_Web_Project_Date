from django import forms

# 별점평가에 사용하기 위해 starWidget 클래스 작성
# forms의 형태를 사용하고 TextInput을 통해 값을 입력받음
class starWidget(forms.TextInput):
    # input_type 설정
    input_type = 'rating'
    # 템플릿 지정
    template_name = "date/star_score.html"

    class Media:
        # 해당 위젯에서 사용할 css, js 불러오기
        css = {
            'all': [
                'widgets/rateit.css',
            ],
        }
        js = [
            "//code.jquery.com/jquery-3.4.1.min.js",
            'widgets/jquery.rateit.min.js',
        ]

    # star_score.html에 사용되는 attr 생성(별의 갯수를 지정하기 위함)
    def build_attrs(self, *args, **kwargs):
        attrs = super().build_attrs(*args, **kwargs)
        # 최소, 0개, 최대 5개, 1칸씩 이동 가능하도록 범위 설정
        attrs.update({
            'min': 0,
            'max': 5,
            'step': 1,
        })
        # attr 값 출력
        return attrs