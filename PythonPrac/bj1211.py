{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "bj1211.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyOoozfUQ1gJlchHVKt+77wv",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/hongseoi/beakjoon-python/blob/main/%EC%86%90%EC%9D%B5%EB%B6%84%EA%B8%B0%EC%A0%90\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#1712 try1\n",
        "A,B,C = map(int, input().split())\n",
        "n = 1\n",
        "while True:\n",
        "    cost = A + B*n\n",
        "    benefit  = C * n\n",
        "    n += 1\n",
        "\n",
        "    if  benefit >= cost:\n",
        "        print(n)\n",
        "        break\n",
        "    else:\n",
        "        print(-1)\n",
        "        break"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ItxKzgre577R",
        "outputId": "cdb3e939-420f-4eb5-d26e-071898ec5e94"
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "100 11 1111\n",
            "2\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#1712 try2\n",
        "def benefit():\n",
        "  a, b, c = map(int, input().split())\n",
        "  n = 0\n",
        "  while True:\n",
        "    if n >= a/(c-b):\n",
        "      return n\n",
        "      break\n",
        "      \n",
        "    else:\n",
        "      n += 1\n",
        "\n",
        "benefit()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "a6n4ly1D6jfp",
        "outputId": "d8e21fbb-edf3-487c-baa6-3893f0dd325c"
      },
      "execution_count": 5,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "100 11 12\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "100"
            ]
          },
          "metadata": {},
          "execution_count": 5
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "A , B, C = map(int, input().split())\n",
        "if B>=C:\n",
        "\tprint(-1)\n",
        "else:\n",
        "\tprint(int(A/(C-B))+1) #정수변환시 소수점 아래가 제거되므로 +1을 해준다."
      ],
      "metadata": {
        "id": "tH5lqVDB9_L_"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#10872\n",
        "\n",
        "n = int(input())\n",
        "count = 0\n",
        "def facto(n):\n",
        "  count += n\n",
        "  n -= 1\n",
        "  facto(n)\n",
        "  if n == 0:\n",
        "    return count\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MtRHjpb0-Jg8",
        "outputId": "fc4c0b7b-c070-4c39-9c59-09a37dd00f86"
      },
      "execution_count": 7,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "10\n"
          ]
        }
      ]
    }
  ]
}
