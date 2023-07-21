import Link from "next/link";
import ProfileIcon from "./ProfileIcon";

export default function Navbar() {
  return (
    <nav className="flex items-center justify-between fixed left-0 right-0 px-8 h-14 bg-black text-white">
      <Link className="text-center font-bold center" href={"/"}>
        StyCheck | 
      </Link>
      <ProfileIcon />
    </nav>
  );
}
