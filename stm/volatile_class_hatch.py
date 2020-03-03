import cv2
import time
import os
import datetime


class VolatileClassHatch(object):
    def __init__(self):
        self.next_state = 'None'
        self._control_frame_count = 0
        self.number_of_egg = 12
        self.hatched_egg = -2
        self.out_key = 'None'
        self.dst = 0
        self.shiny_number = -2
        self.send_command = 'None'
        self.get_shiny_flag = False
        self.shiny_vote = 0
        # self.get_non_shiny_counter = 5
        # self.non_shiny = np.zeros(())
        self.non_shiny_temp = cv2.imread(r"data\non_shiny_template.png")
        self.non_shiny_slash = cv2.imread(r"data\non_shiny_slash.png")
        self.shiny_temp = cv2.imread(r"data\shiny_template.png")

        #print('oya detected.')

    def hatch_command(self, frame):
        if self._control_frame_count == 10:
            self.send_command = 'Button A'
            self._control_frame_count += 1
        # elif self._control_frame_count == 914:
        #     self.detect_shiny(frame)
        #     self._control_frame_count += 1
        elif self._control_frame_count == 918:
            self.detect_shiny(frame)
            self._control_frame_count += 1
        elif self._control_frame_count == 919:
            self.detect_shiny(frame)
            self._control_frame_count += 1
        elif self._control_frame_count == 920:
            self.detect_shiny(frame)
            self._control_frame_count += 1
        elif self._control_frame_count == 921:
            self.detect_shiny(frame)
            self._control_frame_count += 1
        elif self._control_frame_count == 922:
            self.detect_shiny(frame)
            self._control_frame_count += 1
        # elif self._control_frame_count == 924:
        #     self.detect_shiny(frame)
        #     self._control_frame_count += 1
        # elif self._control_frame_count == 926:
        #     self.detect_shiny(frame)
        #     self._control_frame_count += 1
        # elif self._control_frame_count == 928:
        #     self.detect_shiny(frame)
        #     self._control_frame_count += 1
        elif not self.get_shiny_flag:
            if self._control_frame_count == 950:
                self.send_command = 'Button A'
                self._control_frame_count += 1
            elif self._control_frame_count == 970:
                self.send_command = 'Button A'
                self._control_frame_count += 1
            elif not self.get_shiny_flag and self._control_frame_count == 1100:
                self._control_frame_count = 0
                self.hatched_egg = self.hatched_egg + 1
                self.number_of_egg = self.number_of_egg - 1
                self.next_state = 'RUN'
            else:
                self.send_command = 'None'
                self._control_frame_count += 1
        elif self.get_shiny_flag:
            if self._control_frame_count == 1120:
                self.send_command = 'Button A'
                self._control_frame_count += 1
            elif self._control_frame_count == 1320:
                self._control_frame_count += 1
            else:
                if self._control_frame_count > 1320:
                    self.save_game()
                else:
                    self.send_command = 'None'
                    self._control_frame_count += 1

        else:
            self.send_command = 'None'
            self._control_frame_count += 1

    def hatch_action(self, frame):
        self.action_frame = frame
        self.hatch_command(frame)

    def save_game(self):
        if self._control_frame_count == 0 + 1100 + 222:
            self.send_command = 'Button X'
            self._control_frame_count += 1
        elif self._control_frame_count == 3 + 1100 + 222:
            self.send_command = 'STOP'
            self._control_frame_count += 1
        elif self._control_frame_count == 15 + 30 + 1100 + 222:
            self.send_command = 'Button R'
            self._control_frame_count += 1
        elif self._control_frame_count == 17 + 10 + 30 + 1100 + 222:
            self.send_command = 'Button A'
            self._control_frame_count += 1
        elif self._control_frame_count == 19 + 10 + 30 + 30 + 1100 + 222:
            self.send_command = 'STOP'
            self._control_frame_count += 1
        elif self._control_frame_count == 30 + 10 + 30 + 60 + 1100 + 222:
            self.send_command = 'Button A'
            self._control_frame_count += 1
        elif self._control_frame_count == 120 + 30 + 60 + 60 + 1100 + 222:
            self.send_command = 'Button B'
            self._control_frame_count += 1
        elif self._control_frame_count == 125 + 30 + 60 + 60 + 1100 + 222:
            self.send_command = 'STOP'
            self._control_frame_count += 1
        elif self._control_frame_count == 130 + 30 + 60 + 60 + 60 + 1100 + 222:
            self.send_command = 'Button B'
            self._control_frame_count += 1
        elif self._control_frame_count == 131 + 30 + 60 + 60 + 60 + 60 + 1100 + 222:
            self.send_command = 'STOP'
            self._control_frame_count = 0
            self.hatched_egg = self.hatched_egg + 1
            self.number_of_egg = self.number_of_egg - 1
            self.next_state = 'RUN'
            self.get_shiny_flag = False
            print("game saved")
            # self.last_save_time = now
        else:
            self.send_command = 'None'
            self._control_frame_count += 1

    def detect_shiny(self, frame):
        if self.get_shiny_flag == True:
            return

        cv2.rectangle(self.action_frame, (320, 450), (420, 550), (0, 255, 0),
                      2)
        cut_frame_f = frame[450:550, 320:420, ]
        timestr = time.strftime("%Y%m%d-%H%M%S")
        # cv2.imwrite(
        #     'C:\\Users\\wanglamao\\OneDrive\\Playground\\poke-auto-fuka\\shiny\\hatched\\ROI_{}.png'
        #     .format(timestr), cut_frame_f)
        match_non_shiny = cv2.matchTemplate(cut_frame_f, self.non_shiny_temp,
                                            cv2.TM_CCOEFF_NORMED)
        match_non_shiny_slash = cv2.matchTemplate(cut_frame_f,
                                                  self.non_shiny_slash,
                                                  cv2.TM_CCOEFF_NORMED)
        match_shiny = cv2.matchTemplate(cut_frame_f, self.shiny_temp,
                                        cv2.TM_CCOEFF_NORMED)
        _, max_value_non_shiny, _, _ = cv2.minMaxLoc(match_non_shiny)

        _, max_value_non_shiny_slash, _, _ = cv2.minMaxLoc(
            match_non_shiny_slash)
        _, max_value_shiny, _, _ = cv2.minMaxLoc(match_shiny)

        max_value_non_shiny = max(max_value_non_shiny,
                                  max_value_non_shiny_slash)
        print("*********************************")
        print("non_shiny: %f shiny:%f" %
              (max_value_non_shiny, max_value_shiny))
        print("*********************************")

        if max_value_non_shiny < max_value_shiny:
            self.shiny_vote += 1
            if self.shiny_vote >= 1:
                self.shiny_vote = 0
                self.shiny_number = self.shiny_number + 1
                self.get_shiny_flag = True
                with open('shiny/shiny.txt', 'a+') as f:
                    f.writelines(str(datetime.datetime.now()) + "\n")
                    f.writelines("non_shiny: %f shiny:%f" %
                                 (max_value_non_shiny, max_value_shiny) + "\n")
                    f.writelines("\n")
                f.close()
                cv2.imwrite(
                    'C:\\Users\\wanglamao\\OneDrive\\Playground\\poke-auto-fuka\\shiny\\ROI_{}.png'
                    .format(timestr), cut_frame_f)
        # elif 0.8 * max_value_non_shiny < max_value_shiny:
        #     with open('shiny/shiny.txt', 'a+') as f:
        #         f.writelines(str(datetime.datetime.now()) + "\n")
        #         f.writelines("non_shiny: %f shiny:%f" %
        #                      (max_value_non_shiny, max_value_shiny) + "\n")
        #         f.writelines("\n")
        #     f.close()
        #     cv2.imwrite(
        #         'C:\\Users\\wanglamao\\OneDrive\\Playground\\poke-auto-fuka\\shiny\\ROI_{}.png'
        #         .format(timestr), cut_frame_f)

    def state_action(self, frame, key, num_egg, htc_egg, shiny_number):
        self.number_of_egg = num_egg
        self.hatched_egg = htc_egg
        self.action_frame = frame
        self.shiny_number = shiny_number
        self.hatch_action(frame)
        #self.next_state = 'RUN'
