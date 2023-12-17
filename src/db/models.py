from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String
from sqlalchemy.ext.asyncio import AsyncAttrs


class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True
    id: Mapped[int] = mapped_column(primary_key=True)


class Swapi(Base):
    __tablename__ = "swapi_people"

    birth_year: Mapped[str] = mapped_column(nullable=True)
    eye_color: Mapped[str] = mapped_column(nullable=True)
    films: Mapped[str] = mapped_column(nullable=True)
    gender: Mapped[str] = mapped_column(nullable=True)
    hair_color: Mapped[str] = mapped_column(nullable=True)
    height: Mapped[str] = mapped_column(nullable=True)
    homeworld: Mapped[str] = mapped_column(nullable=True)
    mass: Mapped[str] = mapped_column(nullable=True)
    name: Mapped[str] = mapped_column(nullable=True)
    skin_color: Mapped[str] = mapped_column(nullable=True)
    species: Mapped[str] = mapped_column(nullable=True)
    starships: Mapped[str] = mapped_column(nullable=True)
    vehicles: Mapped[str] = mapped_column(nullable=True)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "birth_year": self.birth_year,
            "eye_color": self.eye_color,
            "films": self.films,
            "gender": self.gender,
            "hair_color": self.hair_color,
            "height": self.height,
            "homeworld": self.homeworld,
            "mass": self.mass,
            "name": self.name,
            "skin_color": self.skin_color,
            "species": self.species,
            "starships": self.starships,
            "vehicles": self.vehicles,
        }

    def from_dict(self, data: dict):
        self.id = data.get("id")
        self.birth_year = data.get("birth_year")
        self.eye_color = data.get("eye_color")
        self.films = ",".join(data.get("films")) or ""
        self.gender = data.get("gender")
        self.hair_color = data.get("hair_color")
        self.height = data.get("height")
        self.homeworld = data.get("homeworld")
        self.mass = data.get("mass")
        self.name = data.get("name")
        self.skin_color = data.get("skin_color")
        self.species = ",".join(data.get("species")) or ""
        self.starships = ",".join(data.get("starships")) or ""
        self.vehicles = ",".join(data.get("vehicles")) or ""
        return self
