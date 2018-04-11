from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from queens.forms import IndexForm
from django.views.generic import TemplateView
import copy

class Index(TemplateView):
    template_name = 'queens/index.html'
    def get(self,request):
        form = IndexForm()
        return render(request, self.template_name,{'form':form})

    def post(self,request):
        form = IndexForm(request.POST)
        if form.is_valid():
            size = form.cleaned_data['post']



        def is_safe(board, row, col, size):
            """Check if it's safe to place a queen at board[x][y]"""

            # check row on left side
            for iy in range(col):
                if board[row][iy] == 1:
                    return False

            ix, iy = row, col
            while ix >= 0 and iy >= 0:
                if board[ix][iy] == 1:
                    return False
                ix -= 1
                iy -= 1

            jx, jy = row, col
            while jx < size and jy >= 0:
                if board[jx][jy] == 1:
                    return False
                jx += 1
                jy -= 1

            return True

        def solve(board, col, size):
            """Use backtracking to find all solutions"""
            # base case
            if col >= size:
                return

            for i in range(size):
                if is_safe(board, i, col, size):
                    board[i][col] = 1
                    if col == size - 1:
                        add_solution(board)
                        board[i][col] = 0
                        return
                    solve(board, col + 1, size)
                    # backtrack
                    board[i][col] = 0

        def add_solution(board):
            """Saves the board state to the global variable 'solutions'"""

            saved_board = copy.deepcopy(board)
            solutions.append(saved_board)

        solutions = []

        board = [0] * size
        for ix in range(size):
            board[ix] = [0] * size



        solve(board, 0, size)
        sol_count = len(solutions)
        args = {'form':form,'size':size,'board':board,'solutions':solutions,'sol_count':sol_count}

        return render(request, self.template_name, args)


def testing(request):
    test = ['testing','hello']

    return HttpResponse()