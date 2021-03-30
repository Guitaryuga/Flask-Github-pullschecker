def test_home_page(test_client):
    """
    Тест доступности главной страницы
    """
    response = test_client.get('/')
    assert response.status_code == 200
    assert b'Github Pull checker' in response.data


def test_search(test_client):  # не совсем верный подход
    search = test_client.post('/', data=dict(username='octocat'))
    assert search.status_code == 200
    assert b'Project name' in search.data


"""
There will be more tests here
"""
