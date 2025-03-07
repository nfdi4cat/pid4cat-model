package None;

import java.util.List;
import lombok.*;



/* version: 0.0.0 */


/**
  A URN (Uniform Resource Name).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class UrnIdentifier extends RelatedIdentifier {

  private String identifier;

}
