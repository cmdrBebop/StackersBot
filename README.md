# StackersBot
Application for tracking the skills of students for further invitations for internships and work

## Run

Для развертывания проекта используется Docker. 

- Необходимо установить docker и docker-compose.
- Заполнить .env файлы в соответствии с их шаблонами .env.dist
- Миграции применяются автоматически в entrypoint
- Суперпользователь создается сам, его юзернейм и пароль надо указать в .env

## Contributors
| Person      | GitLab | Role |
| ----------- | ----------- |---|
| Talova Olesya | [ttalova](https://github.com/ttalova) | Team leader |
| Devyatov Konstantin | [cmdrBebop](https://github.com/cmdrBebop) | Tech leader |
| Novak Sergey | [sergeynovak1](https://github.com/sergeynovak1) | Developer |
| Lupanov Bogdan | [VARWA](https://github.com/VARWA) | Developer |
| Evstratova Darya | [DashaEvstratova](https://github.com/DashaEvstratova) | Developer |

## Project tasks
- [X] Track student traffic after educational events, a single database of all participants
- [X] Targeted mailing of invitations to events and internships
- [X] Convenient search for candidates for employment
- [X] All kinds of analysis of the target audience
- [X] Ability to collect data from already held events
