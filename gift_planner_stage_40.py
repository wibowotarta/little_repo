# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: GiftPlanner
import argparse

def main():
    parser = argparse.ArgumentParser(description="GiftPlanner CLI")
    sub = parser.add_subparsers(dest="command")

    p_add = sub.add_parser("add", help="Добавить подарок")
    p_add.add_argument("--name", required=True)
    p_add.add_argument("--recipient", required=True)
    p_add.add_argument("--reason", default="")
    p_add.add_argument("--budget", type=float, default=0.0)

    p_show = sub.add_parser("show", help="Показать подарки")

    p_done = sub.add_parser("done", help="Отметить подарок как купленный")
    p_done.add_argument("--id", required=True)

    args = parser.parse_args()
    if args.command == "add":
        add_gift(args.name, args.recipient, args.reason, args.budget)
    elif args.command == "show":
        show_gifts()
    elif args.command == "done":
        mark_done(int(args.id))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
