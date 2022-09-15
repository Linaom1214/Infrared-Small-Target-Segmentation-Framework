# @Time    : 2022/4/6 19:04
# @Author  : PEIWEN PAN
# @Email   : 121106022690@njust.edu.cn
# @File    : logs.py
# @Software: PyCharm
from datetime import datetime

import os


def save_train_args_log(args, save_dir):
    dict_args = vars(args)
    args_key = list(dict_args.keys())
    args_value = list(dict_args.values())
    with open('work_dirs/%s/train_log.txt' % save_dir, 'a') as f:
        now = datetime.now()
        f.write("time:--")
        dt_string = now.strftime("%Y/%m/%d %H:%M:%S  ")
        f.write(dt_string)
        f.write('\n')
        for i in range(len(args_key)):
            f.write(args_key[i])
            f.write(':--')
            f.write(str(args_value[i]))
            f.write('\n')
        f.write('\n')
    return


def save_train_log(save_dir, epoch, epochs, iter, iters, loss):
    with open('work_dirs/%s/train_log.txt' % save_dir, 'a') as f:
        now = datetime.now()
        dt_string = now.strftime("%Y/%m/%d  %H:%M:%S  ")
        f.write(dt_string)
        f.write('Epoch: [%d/%d]  Iter[%d/%d]  Loss: %.4f' % (epoch, epochs, iter, iters, loss))
        f.write('\n')
    return


def save_test_log(save_dir, epoch, epochs, iter, iters, loss, mIoU, nIoU, f1, best_miou, best_niou, best_f1):
    with open('work_dirs/%s/train_log.txt' % save_dir, 'a') as f:
        now = datetime.now()
        dt_string = now.strftime("%Y/%m/%d  %H:%M:%S  ")
        f.write(dt_string)
        f.write('Epoch: [%d/%d]  Iter[%d/%d]  Loss: %.4f  mIoU: %.4f  nIoU: %.4f  F1-score: %.4f  '
                'Best_mIoU: %.4f  Best_nIoU: %.4f  Best_F1-score: %.4f' % (
            epoch, epochs, iter, iters, loss, mIoU, nIoU, f1, best_miou, best_niou, best_f1))
        f.write('\n')
    return


def save_result_for_test(save_dir, st_model, epochs, mIoU, nIoU, recall, precision, FA, PD, datatset, f1):
    with open('work_dirs/%s/test_log.txt' % save_dir, 'a') as f:
        now = datetime.now()
        dt_string = now.strftime("%Y/%m/%d  %H:%M:%S")
        f.write(dt_string)
        f.write('\n')
        f.write("Model: " + st_model + '\n')
        f.write("Dataset: " + datatset + '\n')
        f.write('Epoch: %d' % (epochs))
        f.write('\n')
        f.write('mIoU: %.4f  nIoU: %.4f  F1-score: %.4f' % (mIoU, nIoU, f1))
        f.write('\n')
        f.write('Recall-----:')
        for i in range(len(recall)):
            f.write('   ')
            f.write(str(round(recall[i], 8)))
            f.write('   ')
        f.write('\n')
        f.write('Precision--:')
        for i in range(len(precision)):
            f.write('   ')
            f.write(str(round(precision[i], 8)))
            f.write('   ')
        f.write('\n')
        f.write('PD---------:')
        for i in range(len(PD)):
            f.write('   ')
            f.write(str(round(PD[i], 8)))
            f.write('   ')
        f.write('\n')
        f.write('FA---------:')
        for i in range(len(FA)):
            f.write('   ')
            f.write(str(round(FA[i], 8)))
            f.write('   ')
        f.write('\n')
        f.write(
            '---------------------------------------------------------------------------------------------------------'
            '---------------------------------------------------------------------------------------------------\n')
        f.write(
            '---------------------------------------------------------------------------------------------------------'
            '---------------------------------------------------------------------------------------------------\n')
        f.write(
            '---------------------------------------------------------------------------------------------------------'
            '---------------------------------------------------------------------------------------------------\n')
    return


def make_dir(dataset, model):
    now = datetime.now()
    dt_string = now.strftime("%Y_%m_%d_%H_%M_%S")
    save_dir = "%s_%s_%s" % (dataset, model, dt_string)
    os.makedirs('work_dirs/%s' % save_dir, exist_ok=True)
    return save_dir
