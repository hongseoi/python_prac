# 패키지 폴더 내부에 존재하며 패키지 관련 처리를 하는 파일
# 어떤 처리를 수행해야 하거나 패키지 내부 모듈을 한꺼번에 가져오고 싶을때 사용

# import 시 불러올 모듈 목록
__all__ = ['module_a', 'module_b']

print('test_package load 완료')