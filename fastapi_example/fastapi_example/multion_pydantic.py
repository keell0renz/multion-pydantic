from typing import Type, TypeVar
from pydantic import BaseModel, ValidationError
from multion.client import MultiOn

T = TypeVar("T", bound=BaseModel)


class MultiOnPydantic(MultiOn):
    def retrieve_with_model(self, output_schema: Type[T], *args, **kwargs) -> T:
        if output_schema:
            schema = output_schema.model_json_schema()

            fields = [
                (
                    name,
                    field["type"],
                    field.get("description", "No description provided."),
                    field.get("examples", ["No example provided."])[0],
                )
                for name, field in schema["properties"].items()
            ]

            cmd = f"{output_schema.__doc__}\nPlease ensure proper typing of the outputs:\n{fields}"
            args_list = list(output_schema.model_json_schema()["required"])

            response = self.retrieve(cmd=cmd, fields=args_list, *args, **kwargs)

            try:
                validated_data = output_schema.model_validate(response.data[0])
                return output_schema(**validated_data.dict())
            except ValidationError as e:
                raise ValidationError() from e

        raise NotImplementedError("You cannot use 'retrieve_with_model' without specifying schema! Use 'retrieve' instead.")


# Attach the method to the MultiOn class
setattr(MultiOn, "retrieve_with_model", MultiOnPydantic().retrieve_with_model)
