package None;

import java.util.List;
import lombok.*;



/* version: 0.0.0 */


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
