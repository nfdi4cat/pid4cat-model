package None;

import java.util.List;
import lombok.*;






/**
  Data class to hold information about the resource and its representation.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ResourceInfo  {

  private String label;
  private String description;
  private String resourceCategory;
  private List<RepresentationVariant> representationVariants;

}
